with open("zphchip_out.h", "wt") as fout:
    with open("zphchip.h", "rt") as fin:
        for line in fin:
            fout.write(line.replace('PECHIP', 'ZPHCHIP'))
            fout.write(line.replace('pechip', 'zphchip'))
            fout.write(line.replace('PE', 'ZPH'))
            fout.write(line.replace('_pe_', '_zph_'))
