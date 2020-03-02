
'''
gale-shapley algo
Define a matching M, is a matching m-w with m element of M and w element of W
For this example we will have 3 m and 3 w
 
Preferences below. We can represent women's preferences in an inverse of their preference list
We can also make a hash map.

 
Ana       Xavier, Zeus,   Yancy*
Bertha    Zeus,   Xavier*, Yancy
Carrie    Yancy,  Zeus*,   Xavier

Xavier    Carrie, Bertha*, Ana
Yancy     Ana*, Bertha, Carrie
Zeus      Carrie*, Ana, Bertha


Maintain a list of wife[] and husband[] where wife[m] = w and husband[w] = m
For sake of simplicty we will use a hashmap to respresent this. Otherwise we could
assign integer IDs to both parties.
'''


ana_pref = {}
ana_pref['Xavier'] = 1
ana_pref['Yancy'] = 3
ana_pref['Zeus'] = 2

bertha_pref = {}
bertha_pref['Xavier'] = 2
bertha_pref['Yancy'] = 3
bertha_pref['Zeus'] = 1

carrie_pref = {}
carrie_pref['Xavier'] = 3 
carrie_pref['Yancy'] = 1
carrie_pref['Zeus'] = 2

women_pref = {}
women_pref['Ana'] = ana_pref
women_pref['Bertha'] = bertha_pref
women_pref['Carrie'] = carrie_pref

wife = {}
wife['Xavier'] = 0
wife['Yancy'] = 0
wife['Zeus'] = 0

husband = {}
husband['Ana'] = 0
husband['Bertha'] = 0
husband['Carrie'] = 0

propose_count = {}
propose_count['Xavier'] = 0
propose_count['Yancy'] = 0
propose_count['Zeus'] = 0

xavier_pref = ['Carrie', 'Bertha', 'Ana']
yancy_pref = ['Ana', 'Bertha', 'Carrie']
zeus_pref = ['Carrie', 'Ana', 'Bertha']

men_pref = {}
men_pref['Xavier'] = xavier_pref
men_pref['Yancy'] = yancy_pref
men_pref['Zeus'] = zeus_pref

free_man_queue = ['Zeus', 'Xavier', 'Yancy']

def isSomeManFree():
    '''
    Desc:
        Find existence of unpaired man whom hasn't asked all women out already.
    Return:
        Man string if some man is free, else if all men are paired return None
    '''
    
    if free_man_queue:
        return free_man_queue.pop()
    else:
        return None

def main():
    while(True):
        man = isSomeManFree()
        if not man:
            break
        # first access returns given man's ordered preference list, second access returns which woman he is at
        woman = men_pref[man][propose_count[man]] 
        print('\n%s and %s' % (man, woman))
        
        # If woman is free, pair man and woman
        if husband[woman] == 0:
            print('Man: %s pairs with woman: %s' % (man, woman))
            wife[man] = woman
            husband[woman] = man

        # If woman prefers this man over her current man
        elif women_pref[woman][man] < women_pref[woman][husband[woman]]:
            print('Woman: %s prefers man: %s over %s' % (woman, man, husband[woman]))
            print('%d preferred before %d ' % (women_pref[woman][man], women_pref[woman][husband[woman]]))
            wife[husband[woman]] = 0    # free her assigned man
            free_man_queue.append(husband[woman]) # add to queue of free men

            # pair man and woman
            wife[man] = woman           
            husband[woman] = man       
        
        # else she rejects man
        else:
            print('Woman: %s rejects man: %s' % (woman, man))
            free_man_queue.append(man) # add to queue of free men


        propose_count[man] += 1 
    
    print('\n--------------------------\nMatchings:')
    print(husband)
    print(wife)  

if __name__ == "__main__":
    main()