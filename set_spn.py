def set_spn(toponym):
    coord = toponym["boundedBy"]["Envelope"]
    long_min, latt_min = coord["lowerCorner"].split(" ")
    long_max, latt_max = coord["upperCorner"].split(" ")
    return str(float(long_max) - float(long_min)), str(float(latt_max) - float(latt_min))