#!/usr/bin/env python
# coding: utf-8

# Project
# 

# In[ ]:


import string
import random


# In[ ]:


# information about emotion input and corresponding emotion output#
greetings_in = ['hi','hello','hola','is anyone there','how are you']
greetings_out = ['Hi','Good to see you','how can i help you?','good to see you']
QUESTION  = "I'm too shy to answer questions. Ask me other thing."
unknown_out = ['sorry, i dont understand','what is that?','ummmm']
goodbye = ['bye','goodbye','see you next time','ok, bye']

# information about animals' species, role, personality. 
Alligator = {'Alfonso':'lazy','Alli':'snooty','Del':'cranky','Drago':'lazy','Gayle':'normal','Sly':'jock'}
Bear = {'Curt':'cranky','Grizzly':'cranky','Groucho':'cranky','Beardo':'smug','Charlise':'sisterly','Chow':'cranky','Nate':'lazy','Paula':'sisterly','Pinky':'peppy','Klaus':'smug','Teddy':'jock','Tutu':'peppy'}
Bird = {'Jitters':'jock','Jay':'jock','Jacques':'smug','Anchovy':'lazy','Peck':'jock','Lucha':'smug','Midge':'normal','Sparro':'jock','Robin':'snooty','Twiggy':'peppy'}
Cat = {'Katt':'sisterly','Kabuki':'cranky','Felicity':'peppy','Ankha':'snooty','Bob':'lazy','Monique':'snooty','Olivia':'snooty','Kitty':'snooty','Kiki':'normal','Lolly':'normal','Kid Cat':'jock','Merry':'peppy','Rosie':'peppy','Rudy':'jock','Purri':'snooty','Punchy':'lazy','Tom':'cranky'}
Cub = {'Barold':'lazy','Bluebear':'peppy','Chester':'lazy','Cheri':'peppy','Poncho':'jock','Pekoe':'normal','Kody':'jock','Maple':'normal','Pudge':'lazy'}
Dog = {'Goldie':'normal','Daisy':'normal','Biskit':'lazy','Benjamin':'lazy','Butch':'cranky','Bones':'lazy','Cherry':'sisterly','Portia':'snooty','Lucky':'lazy','Marcel':'lazy','Mac':'jock','Shep':'smug','Walker':'lazy'}
Eagle = {'Keaton':'smug','Frank':'cranky','Avery':'cranky','Amelia':'snooty','Apollo':'cranky','Celia':'normal','Pierce':'jock','Sterling':'jock'}

    


# In[ ]:


#from A3:
def string_concatenator ( string1, string2, separator):
    """Adds strings together with separator between them
    Parameters
    ----------
    string1: string
        The front string to add 
    string2: string
        The following string to add
    separator: string 
        The string that goes between two strings
    Returns
    -------
    output: string
        Added string of two strings 
    """
    output = string1+separator+string2
    return output


# In[ ]:


def list_to_string(input_list, separator):
    """Helper method to change the list to string with separator between them
    Parameters
    ----------
    input_list: list
        list that contains user input
    separator: string
        A string that goes between each string 
    Returns
    -------
    output: string
        String representation of the list with separator 
    """
    output = input_list[0]
    for i in input_list[1:]:
        output = string_concatenator(output, i, separator)
    return output


# In[ ]:



def prepare_text(input_string):
    """Helper method to make the input lower case and split multiple strings
    Got rid of remove_punctuation from org because some inputs need to contain '
    Parameters
    ----------
    input_string: string
        A string that user input 
    Returns
    -------
    out_list: list
        List representation of input after modifying
    """
    out_list = []
    temp_string = ''
    temp_string = input_string.lower()
    out_list = temp_string.split()
    return out_list


# In[ ]:


def end_chat (input_list):
    """Ends the chat if the input matches 'quit' or 'exit'
    Parameters
    ----------
    input_list: list
        the list that contains user input
    Returns
    -------
        boolean
    Whether the input was quit or exit or none 
    """
    for item in input_list:
        if item.lower() == 'quit' or item.lower() == 'exit':
            return True
        else: 
            return False


# In[ ]:


def is_in_list(list_one, list_two):
    """ Check if any element of list_one is in list_two.
    Parameters
    ----------
    list_one: list 
        List to check if its inside the two
    list_two: list
        List to see if one belongs inside 
        
    Returns
    -------
            boolean
        Boolean whether list_one exists or not 
    """
    for element in list_one:
        if element in list_two:
            return True
    return False


# In[ ]:


# self-define functions
def start():
    """" function to print my first message for users"""
    print('Welcome to AnimalBot. I will help you with the basic information about the animal roles in Animal Crossing:)')
    print( 'What do you want to know? Choose one among role, species or personality. ')


def is_List(input_list):
    """ Checks if the user ask to show a 'list' of anything
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = ''
    check = list_to_string(input_list,' ')
    if check.lower() == 'list':
            return True
    return False

# In[ ]:
def dict_of_anim():
    """Creates a dictionary of all animal's species dictionary
    Returns
    -------
    list_Dict: dictionary 
        dictionary that contains a dictionary of all species dictionary 
    """
    list_dict = {}
    list_dict.update({'Alligator':Alligator})
    list_dict.update({'Bear':Bear})
    list_dict.update({'Bird':Bird})
    list_dict.update({'Cat':Cat})
    list_dict.update({'Cub':Cub})
    list_dict.update({'Dog':Dog})
    list_dict.update({'Eagle':Eagle})
    return list_dict

def is_personality (input_list):
    """ Checks if the input is 'personality'
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """

    check = list_to_string(input_list,' ')
    if check.lower() == 'personality':
        return True
    return False

# In[ ]:


def is_personality_animal(input_list):
    """ Checks if the input is one particular animal's personality
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input belongs in one of the roles or not 
    """
    dicts = dict_of_anim()
    check = list_to_string(input_list,' ')
    
    #Loop through the dictionary of species and loop through the inner dictionaries.
    for spe in dicts.keys():
        for a in dicts[spe]:
            if check.lower() == dicts[spe].get(a).lower():
                return True
    return False 


# In[ ]:


def more(input_list):
    """ Checks if the user wants to know more
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = list_to_string(input_list,' ')
    if check.lower() == 'yes':
        return True
    return False


# In[ ]:


def is_species(input_list):
    """ Checks if the input was 'species'
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = list_to_string(input_list,' ')
    if check.lower() == 'species':
        return True
    return False


# In[ ]:


def is_species_animal(input_list):
    """ Checks if the input is one of the species 
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is one of the species or not
    """
    dicts = dict_of_anim()
    check = list_to_string(input_list,' ')
    #Checks the key of outer species dictionary 
    for spe in dicts.keys():
        if spe.lower() == check.lower():
            return True
    return False


# In[ ]:


def is_role (input_list):
    """ Checks if the input is 'role'
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = list_to_string(input_list,' ')
    if check.lower() == 'role':
        return True
    return False

def is_role_animal(input_list):
    """checks if input is one of the roles
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is one of the roles or not"""
    dicts = dict_of_anim()
    check = list_to_string(input_list,' ')
    #loop through each species and then loop through inner dictionaries
    for ea in dicts.keys():
        for i in dicts[ea].keys():
            if i.lower() == check.lower():
                return True
    return False



# In[ ]:


def species_of_animal():
    """Creates a string with all species of animal
    Returns
    -------
    classes: string 
        String of all species 
    """
    diction = dict_of_anim()
    species = ''
    #Access the dictionary of species to return 
    for animal in diction.keys():
        species = species + animal +", "
    species = species[:-1]
    return species



# In[ ]:


def get_personality(role):
    """Gets the personality of specific role 
    Parameters
    ----------
    key: list
        list that contains input
    Returns
    -------
    diction[ea].get(a): string
        String of role correspond to the input personality
    """
    diction = dict_of_anim()
    check = list_to_string(role,'')
    #Loop through the dictionary of species to find the inner corresponding key's value 
    for spe in diction.keys():
        for a in diction[spe]:
            if a.lower() == check.lower():
                return diction[spe].get(a)


# In[ ]:


def get_Species(role):
    """Gets the species of specific role
    Parameters
    ----------
    key: list
        list that contains input
    Returns
    -------
    ea: string
        String that contains species information of input role
    """
    diction = dict_of_anim()
    check = list_to_string(role,'')
    for spe in diction.keys():
        for a in diction[spe]: 
            if a.lower() == check.lower():
                return spe

# In[ ]:


def get_personality_role(personality):
    """Gets roles that have certain personality
    Parameters
    ----------
    key: list
        list that contains input
    Returns
    -------
    characters: string
        String that contains role name with certain personality 
    """

    diction = dict_of_anim()
    check = list_to_string(personality,'')
    roles =''

    #Used string because there can be multiple characters with same personality. 
    for spe in diction:
        for a in diction[spe]:
            #Checks the inner dictionary's value to see if the role matches input 
                if diction[spe][a].lower() == check.lower():
                    roles = roles + a + ','
    return list_to_string(roles[:-1],'')


# In[ ]:


def get_role_species(species):
    """Gets roles that has certain species
    Parameters
    ----------
    key: list
        list that contains input
    Returns
    -------
    characters: string
        String that contains personality with certain species 
    """
    diction = dict_of_anim()
    check = list_to_string(species,'')
    roles =''
    #Used string because there can be multiple characters with same class
    for spe in diction:
        for a in diction[spe]:
            if spe.lower()== check.lower():
                roles = roles + a + ', '
                
    #Removes comma at the end 
    roles = roles[:-1]
    return roles


# In[ ]:



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




