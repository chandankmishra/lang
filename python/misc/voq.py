def get_ts_mask_from_vpfe_voq_group(vpfe_14, voq_group_id, num_oq_per_port):
    first = (vpfe_14 << 10) & 0x00FFFC00
    second = (voq_group_id << 6) & 0x000003C0
    return first | second | num_oq_per_port

def get_vpfe_id(ts_mask):
    tmp = ts_mask & 0x00FFFC00
    return tmp >> 10

def get_voq_group(ts_mask):
    tmp = ts_mask & 0x000003C0 
    return tmp >> 6

def get_ts_mask_vpfe_voq_group(stream_num):
    vpfe_14 = stream_num // 4
    vpfe_14 += vpfe_14 // 3
    voq_group_id = stream_num % 4

    ts_mask = get_ts_mask_from_vpfe_voq_group(vpfe_14, voq_group_id, 8)
    vpfe_id = get_vpfe_id(ts_mask)
    voq_group = get_voq_group(ts_mask)
    return ts_mask, vpfe_id, voq_group

print ("stream", "\t", "mask", "\t", "vpfe", "\t", "voq_group", "\t", "base_voq")

for stream in range(80):
    ts_mask, vpfe_id, voq_group = get_ts_mask_vpfe_voq_group(stream)
    vpfe = stream // 4
    print (stream, "\t", ts_mask, "\t", vpfe_id, "\t", voq_group, "\t\t", vpfe * 64 + (stream % 4) * 8)
