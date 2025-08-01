import ipaddress
import pandas as pd
import numpy as np

df = pd.read_excel('ip_data.xlsx')
#print(df.head())

network_addresses = []
broadcast_addresses = []
cidr_notations = []
usable_hosts = []

for _, row in df.iterrows():
    ip = row['IP Address']
    mask = row['Subnet Mask']

    try:
        network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
        net_addr = str(network.network_address)

        broad_addr = str(network.broadcast_address)

        cidr_not = str(network.with_prefixlen)

        if network.prefixlen < 31:
            hosts = network.num_addresses - 2
        else:
            hosts = network.num_addresses

    except Exception as e:
        net_addr = f"Error: {e}"
        broad_addr = f"Error: {e}"
        cidr_not = f"Error: {e}"
        hosts = np.nan

    network_addresses.append(net_addr)
    broadcast_addresses.append(broad_addr)
    cidr_notations.append(cidr_not)
    usable_hosts.append(hosts)


df['Network Address'] = network_addresses
df['Broadcast Address'] = broadcast_addresses
df['CIDR Notation'] = cidr_notations
df['Usable Hosts'] = usable_hosts

#print(df)

df.to_excel('subnet_report.xlsx', index=False)
df.to_csv('subnet_report.csv', index=False)
df.to_json('subnet_report.json', orient='records')

print("Summary generated: subnet_report.xlsx, subnet_report.csv, subnet_report.json")


group_sizes = df.groupby('CIDR Notation').size().reset_index(name='Count')
group_sizes.to_csv('group_sizes.csv', index=False)



# create subnet objects from CIDR notations
subnets = [ipaddress.IPv4Network(cidr, strict=False) for cidr in df['CIDR Notation']]

# compare each pair for overlaps
overlapping_pairs = []
for i in range(len(subnets)):
    for j in range(i + 1, len(subnets)):
        if subnets[i].overlaps(subnets[j]):
            overlapping_pairs.append((str(subnets[i]), str(subnets[j])))

if overlapping_pairs:
    for pair in overlapping_pairs:
        print(f"{pair[0]} overlaps with {pair[1]}")
else:
    print("No overlapping subnets detected.")



# largest subnet
largest_subnet = df.loc[df['Usable Hosts'].idxmax()]
print(largest_subnet)
# smallest subnet
smallest_subnet = df.loc[df['Usable Hosts'].idxmin()]
print(smallest_subnet)