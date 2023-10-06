import psutil

# Get the partitions on the system
partitions = psutil.disk_partitions(all=True)

# Print the names of the drives and the number of drives
drive_names = []
for partition in partitions:
    if partition.device not in drive_names:
        drive_names.append(partition.device)
        print(f"Drive {len(drive_names)}: {partition.device}")

print(f"\nTotal number of drives: {len(drive_names)}")
