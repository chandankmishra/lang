def get_voq_vpfe(asic_id, stream_id):
    vpfe_base = asic_id * 28 
    oq_grp = stream_id % 4
    vpfe = stream_id // 4
    vpfe += vpfe_base + vpfe // 3
    update = ((vpfe & 0x3FFF) << 5) | (oq_grp & 0x1f)
    word4 = 0x20010000 | update 
    print (asic_id, "\t\t", stream_id, "\t\t", oq_grp, "\t\t", vpfe, "\t\t", update, "0x{0:0{1}X}".format(update,4), "\t", hex(word4))


print ("asic_id", "\t", "stream_id", "\t", "oq_grp", "\t", "vpfe", "\t\t", "eg_port_id", "\t", "nh_word") 
for a in range(3):
    for i in range(12):
        get_voq_vpfe(a, i)
