# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:31:44 2019

@author: evinb
"""

class uf:
    
    def __init__(self,elementList):
        self.elements = {}
        self.element_list = elementList
        for ele in elementList:
            self.elements[ele] = self.element(ele)
        self.length = len(elementList)
        
    def uf_print(self):
        for ele in self.elements:
            print(self.elements[ele].id, self.elements[ele].parent_id, self.elements[ele].rank)
        print()
    
    def get_element(self,ident):
        return ((self.elements[ident].id,self.elements[ident].parent_id,self.elements[ident].rank))
    
    def get_elements(self):
        result = []
        for i in self.element_list:
            result.append(self.get_element(i))
        return (result)
    
    """ ident is the element id value rather than an object """
    def find(self, ident):   
        if self.elements[ident].id == self.elements[ident].parent_id:
            return self.elements[ident].id
        else:
            self.elements[ident].parent_id = self.find(self.elements[ident].parent_id)
            #self.elements[ident].rank = 0
            return self.elements[ident].parent_id
        
    def union(self, v1, v2):
        root_v1 = self.find(v1)
        root_v2 = self.find(v2)
        if root_v1 != root_v2:
            if self.elements[root_v1].rank > self.elements[root_v2].rank:
                self.elements[root_v2].parent_id = root_v1
            elif self.elements[root_v2].rank > self.elements[root_v1].rank:
                self.elements[root_v1].parent_id = root_v2
            else:
                self.elements[root_v1].parent_id = root_v2
                self.elements[root_v2].rank += 1
            self.length -= 1
            return True
        else:
            return False
        
    class element:
        def __init__(self,ident):
            self.id = ident
            self.parent_id = ident
            self.rank = 0
   
    
def mst_algo(locs, dist):
    
    name_or_team = 'evinsmith'
    mst = []

    myUF = uf([x for x in locs])
    edges =[[v,k] for k,v in dist.items()]
    edges.sort()
    
    for edge in edges :
        newEdge = myUF.union(edge[1][0], edge[1][1])
        if newEdge:
            mst.append(edge[1])
                
    return name_or_team, mstclass uf:
    
    def __init__(self,elementList):
        self.elements = {}
        self.element_list = elementList
        for ele in elementList:
            self.elements[ele] = self.element(ele)
        self.length = len(elementList)
        
    def uf_print(self):
        for ele in self.elements:
            print(self.elements[ele].id, self.elements[ele].parent_id, self.elements[ele].rank)
        print()
    
    def get_element(self,ident):
        return ((self.elements[ident].id,self.elements[ident].parent_id,self.elements[ident].rank))
    
    def get_elements(self):
        result = []
        for i in self.element_list:
            result.append(self.get_element(i))
        return (result)
    
    """ ident is the element id value rather than an object """
    def find(self, ident):   
        if self.elements[ident].id == self.elements[ident].parent_id:
            return self.elements[ident].id
        else:
            self.elements[ident].parent_id = self.find(self.elements[ident].parent_id)
            #self.elements[ident].rank = 0
            return self.elements[ident].parent_id
        
    def union(self, v1, v2):
        root_v1 = self.find(v1)
        root_v2 = self.find(v2)
        if root_v1 != root_v2:
            if self.elements[root_v1].rank > self.elements[root_v2].rank:
                self.elements[root_v2].parent_id = root_v1
            elif self.elements[root_v2].rank > self.elements[root_v1].rank:
                self.elements[root_v1].parent_id = root_v2
            else:
                self.elements[root_v1].parent_id = root_v2
                self.elements[root_v2].rank += 1
            self.length -= 1
            return True
        else:
            return False
        
    class element:
        def __init__(self,ident):
            self.id = ident
            self.parent_id = ident
            self.rank = 0
   
    
def mst_algo(locs, dist):
    
    name_or_team = 'evinsmith'
    mst = []

    myUF = uf([x for x in locs])
    edges =[[v,k] for k,v in dist.items()]
    edges.sort()
    
    for edge in edges :
        newEdge = myUF.union(edge[1][0], edge[1][1])
        if newEdge:
            mst.append(edge[1])
                
    return name_or_team, mst