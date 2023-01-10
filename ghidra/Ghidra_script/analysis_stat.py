import os
def get_compiler_spec():
    return currentProgram.getCompilerSpecID().toString()

def get_function_count():
    return currentProgram.getFunctionManager().getFunctionCount()

def get_import_api_count():
    ext_symbols = currentProgram.getSymbolTables().getExternalSymbols()
    return len(list(ext_symbols))
  
def get_defined_data_count():
    exec_memsets = currentProgram.getMemory().getExecuteSet()
    data = currentProgram.getListing().getData(exec_memsets, True)
    return sum([len(d.getBytes()) for d in data if d.isDefined()])
  
def main():
    stats = dict()
    
    stats['name'] = os.path.basename(currentProgram.getExecutablePath())
    stats['sha256'] = currentProgram.getExecutableSHA256()
    stats['language'] = currentProgram.getLanguageID().toString()
    stats['compiler_spec'] = get_compiler_spec()
    stats['function_count'] = get_function_count()
    stats['import_api_count'] = get_import_api_count()
    stats['defined_data_count'] = get_defined_data_count()
    
    for key, value in stats.items():
        print('{}: {}'.format(key, value))
        
if __name__ == '__main__':
    main()