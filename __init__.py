from binaryninja import *
from syms2elf import *

def get_bn_symbols(bv):
    symbols = []
    for func in bv.functions:
        fcn_name = func.name
        fcn_offset = func.start
        fcn_end = max(bb.end for bb in func.basic_blocks)
        fcn_size = fcn_end - fcn_offset
        fcn_section = bv.get_sections_at(fcn_offset)[0].name
        symbols.append(Symbol(fcn_name, STB_GLOBAL_FUNC, fcn_offset, fcn_size, fcn_section))
    return symbols

def export_syms_to_elf(bv):
    symbols = get_bn_symbols(bv)
    newname = interaction.get_save_filename_input("Save to file")
    write_symbols(bv.file.filename, newname, symbols)

PluginCommand.register("Syms2Elf", "Export symbols to ELF", export_syms_to_elf)
