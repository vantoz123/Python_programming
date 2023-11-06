# a program to convert month names to full

monthdict = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May ":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sept":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

print(monthdict["Dec"])
print(monthdict.get("Las"))# You can also use this method to access what is in the dictionary