import csv
from collections import defaultdict

def load_lookup_table(file_path):
    # Initialize an empty dictionary to store the lookup table
    lookup = {}
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Create a tuple key of (port, protocol) and map it to the tag
            key = (int(row['dstport']), row['protocol'].lower())
            lookup[key] = row['tag'].lower()
    return lookup

def process_flow_logs(log_file, lookup_table):
    # Initialize defaultdicts to count tags and port/protocol combinations
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    
    with open(log_file, 'r') as f:
        for line in f:
            # Split each line 
            fields = line.strip().split()
            if len(fields) < 14:
                continue 
            
            # Extract destination port and protocol from the log entry
            dstport = int(fields[5])
            protocol = 'tcp' if fields[7] == '6' else 'udp' if fields[7] == '17' else 'icmp'
            
            # Create a key for lookup and get the corresponding tag
            key = (dstport, protocol)
            tag = lookup_table.get(key, 'Untagged').lower()
            
            # Increment counters for tags and port/protocol combinations
            tag_counts[tag] += 1
            port_protocol_counts[key] += 1
    
    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, output_file):
    with open(output_file, 'w') as f:
        # Write tag counts
        f.write("Tag Counts:\n")
        f.write("Tag,Count\n")
        for tag, count in tag_counts.items():
            f.write(f"{tag},{count}\n")
        
        # Write port/protocol combination counts
        f.write("\nPort/Protocol Combination Counts:\n")
        f.write("Port,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            f.write(f"{port},{protocol},{count}\n")

def main():
    
    lookup_table = load_lookup_table('lookup_table.csv')
    # Process the flow logs
    tag_counts, port_protocol_counts = process_flow_logs('flow_logs.txt', lookup_table)
    # Write the output to a file
    write_output(tag_counts, port_protocol_counts, 'output.txt')

if __name__ == "__main__":
    main()