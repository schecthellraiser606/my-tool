dangerous_func = ['getpw', 'gets', 'sprintf', 'strcat', 'strcpy', 'vsprintf']

def list_xrefs_call_function(func_name):
    manager = currentProgram.getFunctionManager()
    for func in manager.getFunctions(True):
        if func.getName() in func_name:
            for xref in getReferencesTo(func.getEntryPoint()):
                if xref.getReferenceType().toString() == 'UNCONDITIONAL_CALL':
                    print('{} is called at {}'.format(func.getName(), xref.getFromAddress()))
                    
if __name__ == '__main__':
    list_xrefs_call_function(dangerous_func)