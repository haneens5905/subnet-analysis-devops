# Analysis Questions

## 1. Which subnet has the most hosts?

The subnet with the largest number of usable IPs is:

**192.168.100.7/22** → **1,022 usable hosts**


---

## 2. Are there any overlapping subnets? If yes, which ones?

After analyzing all subnet ranges using Python’s `ipaddress.overlaps()` method, **no overlapping subnets were detected**. Each CIDR block in the dataset was unique and non-intersecting.


---

## 3. What is the smallest and largest subnet in terms of address space?

| Type         | Subnet                 | Usable Hosts |
|--------------|------------------------|--------------|
| **Smallest** | `10.50.2.7/24`         | 254          |
| **Largest**  | `192.168.100.7/22`     | 1,022        |


---

