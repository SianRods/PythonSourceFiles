sample_list=   ['0x3cfb','0xcbf8','0x2e51','0xcf89','0x7954', '0x2e51','0x3cfb','0x35c2', '0xd375','0x9a5b','0xf1b8', '0x57c5','0xfd54',
                 '0xd266','0x7954','0xfa47', '0x6ee8', '0x813b', '0x12c3', '0x9a5b']


def FullyAssociativeMapping(reference_list,cache_size):
    
    hit =0
    fault=0
    cache_memory=[]

    for i in reference_list:
        if i in cache_memory:
            hit+=1
            cache_memory.remove(i)
            cache_memory.append(i)
            print(f"List : {cache_memory}")
        else:
            if len(cache_memory)==cache_size:
                fault+=1
                cache_memory.pop(0)
                cache_memory.append(i)
                print(f"List : {cache_memory}")
            
            else:
                fault+=1
                cache_memory.append(i)
                print(f"List : {cache_memory}")
                
    print("Number of Hits are : ",hit)
    print("Number of Faults are :",fault)

cache_size=int(input("Enter the size of the cache memory in no of lines available :"))
FullyAssociativeMapping(sample_list,cache_size)

