#!/bin/bash

# Variables (Modify as needed)
POOL_NAME="mypool"
DATASET_NAME="$POOL_NAME/mydataset"
CLONE_NAME="$POOL_NAME/clone"
MOUNT_DIR="/zfs-mount"
CLONE_MOUNT_DIR="/zfs-clone"
CONTAINER_NAME="zfs-demo"
DEVICE="/dev/sdX"  # Replace with the actual device or a loopback device for testing

# Step 1: Install Required Packages
echo "Installing necessary packages..."
apt update
apt install -y zfsutils-linux docker.io podman

# Step 2: Create ZFS Pool and Dataset
echo "Creating ZFS pool and dataset..."
zpool create $POOL_NAME $DEVICE
zfs create $DATASET_NAME

# Step 3: Set Up the Mount Point
echo "Setting up the mount point..."
mkdir -p $MOUNT_DIR
zfs set mountpoint=$MOUNT_DIR $DATASET_NAME

# Step 4: Run Container with ZFS Mount
echo "Running a container with the ZFS dataset mounted..."
docker run -v $MOUNT_DIR:/data --name $CONTAINER_NAME -d ubuntu sleep infinity

# Step 5: ZFS Snapshots Demo
echo "Demonstrating ZFS snapshots..."
docker exec $CONTAINER_NAME bash -c "echo 'This is a test file' > /data/testfile.txt"
docker exec $CONTAINER_NAME bash -c "echo 'Another test file' > /data/file2.txt"
docker exec $CONTAINER_NAME bash -c "mkdir /data/testdir && echo 'Inside file' > /data/testdir/insidefile.txt"
zfs snapshot $DATASET_NAME@initial
docker exec $CONTAINER_NAME bash -c "echo 'This content has been changed' > /data/testfile.txt && rm /data/file2.txt"
zfs snapshot $DATASET_NAME@modified
echo "Rolling back to initial snapshot..."
zfs rollback $DATASET_NAME@initial

# Step 6: Enable and Test Compression
echo "Enabling compression on the dataset..."
zfs set compression=lz4 $DATASET_NAME
docker exec $CONTAINER_NAME bash -c "dd if=/dev/zero of=/data/bigfile bs=1M count=100"
zfs get compression,compressratio $DATASET_NAME

# Step 7: Enable and Test Deduplication (Optional)
echo "Enabling deduplication..."
zfs set dedup=on $DATASET_NAME
docker exec $CONTAINER_NAME bash -c "cp /data/bigfile /data/duplicate1 && cp /data/bigfile /data/duplicate2"
zfs get dedup,used $DATASET_NAME

# Step 8: Clone Demo
echo "Creating a snapshot and clone..."
zfs snapshot $DATASET_NAME@clonesnapshot
zfs clone $DATASET_NAME@clonesnapshot $CLONE_NAME
mkdir -p $CLONE_MOUNT_DIR
zfs set mountpoint=$CLONE_MOUNT_DIR $CLONE_NAME
docker run -v $CLONE_MOUNT_DIR:/data --name ${CONTAINER_NAME}_clone -d ubuntu sleep infinity

# Step 9: Data Integrity Verification
echo "Simulating data corruption and running a scrub..."
dd if=/dev/urandom of=$MOUNT_DIR/testfile.txt bs=1M count=1 seek=0 conv=notrunc
zpool scrub $POOL_NAME
zpool status $POOL_NAME

# Step 10: Optional - Replication (Requires SSH and Remote Host Configuration)
REMOTE_HOST="user@remote-host"
REMOTE_POOL="remotepool"
echo "Sending snapshot to remote host for replication (this requires setup on the remote host)..."
zfs send $DATASET_NAME@initial | ssh $REMOTE_HOST "zfs receive $REMOTE_POOL/replica"

# Step 11: Cleanup
echo "Cleaning up containers and ZFS pools..."
docker rm -f $CONTAINER_NAME ${CONTAINER_NAME}_clone
zfs destroy $DATASET_NAME@initial
zfs destroy $DATASET_NAME@modified
zfs destroy $CLONE_NAME
zfs destroy $DATASET_NAME
zpool destroy $POOL_NAME

echo "ZFS demo completed!"
