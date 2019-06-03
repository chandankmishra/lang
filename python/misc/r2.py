#!/usr/bin/python
#find * | grep "/"|awk '{printf "mv "$0; gsub("zphchip", "zhchip", $0);print " "$0;}'|sh
import os

def inplace_change(filename, old_string, new_string):
        s=open(filename).read()
        if old_string in s:
                print 'Changing "{old_string}" to "{new_string}"'.format(**locals())
                s=s.replace(old_string, new_string)
                f=open(filename, 'w')
                f.write(s)
                f.flush()
                f.close()
        else:
                print 'No occurances of "{old_string}" found.'.format(**locals())

def replace_file(filename):
    inplace_change(filename, "_ZPH(", "_ZH(")
    inplace_change(filename, "_ZPH_", "_ZH_")
    inplace_change(filename, "_zph(", "_zh(")
    inplace_change(filename, "_zph_", "_zh_")
    inplace_change(filename, "\"zph.", "\"zh.")
    inplace_change(filename, " ZPH_", " ZH_")
    inplace_change(filename, "{ZPH_", "{ZH_")
    inplace_change(filename, "{zph_", "{zh_")
    inplace_change(filename, " ZPH ", " ZH ")
    inplace_change(filename, " zph_", " zh_")
    inplace_change(filename, " zph ", " zh ")
    inplace_change(filename, "(ZPH_", "(ZH_")
    inplace_change(filename, "(ZPH ", "(ZH ")
    inplace_change(filename, "(zph_", "(zh_")
    inplace_change(filename, "(zph ", "(zh ")
    inplace_change(filename, "ZPHCHIP", "ZHCHIP")
    inplace_change(filename, "zphchip", "zhchip")
    inplace_change(filename, "(ZPHCHIP", "(ZHCHIP")
    inplace_change(filename, "(zphchip", "(zhchip")

#    inplace_change(filename, "PIZH", "PIZPH")
#    inplace_change(filename, "REZHAT", "REZPHAT")
#    inplace_change(filename, "TYZH", "TYZPH")
#    inplace_change(filename, "SZHED", "SZPHED")
#    inplace_change(filename, "SZHCIAL", "SZPHCIAL")
#    inplace_change(filename, "SWAPZHD", "SWAPZPHD")
#    inplace_change(filename, "MZHRR", "MZPHRR")
#    inplace_change(filename, "LVZHCL", "LVZPHCL")
#    inplace_change(filename, "pizh", "pizph")
#    inplace_change(filename, "rezhat", "rezphat")
#    inplace_change(filename, "tyzh", "tyzph")
#    inplace_change(filename, "szhed", "szphed")
#    inplace_change(filename, "szhcial", "szphcial")
#    inplace_change(filename, "swapzhd", "swapzphd")

l = os.listdir(os.getcwd())
for i in l:
    replace_file(i)
