l_info = {
    "name": "Tree generator",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy
import math
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

class TreeNode:
    def __init__(self, x, y, z, v, g):
        self.x = x
        self.y = y
        self.z = z
        self.vector = Vector((x,y,z))
        self.index = 0
        self.variation = v
        self.generation = g
        self.childs = []
        
    def __str__(self):
        return str(self.x)
            
    def addChild(self,limit,nodelist):
        if limit == self.generation:
            return 0
        if (len(self.childs) < self.variation) and (self.variation != 2):
            nodeX = math.cos(math.radians(360/self.variation*len(self.childs)))*100-self.generation+1
            nodeY = math.sin(math.radians(360/self.variation*len(self.childs)))*100-self.generation+1
            node = TreeNode( self.x + nodeX , self.y + nodeY , self.z+self.generation*50 , self.variation-1, self.generation+1)
            self.childs.append(node)
            nodelist.append(node)
            nodeIndex = nodelist.index(node)
            nodelist[nodeIndex].index = nodeIndex
            return 1
        else:
            for node in self.childs:
                if node.addChild(limit,nodelist) == 1:
                    return 1
            return 0                      

class Tree(Operator, AddObjectHelper):
    bl_idname = "mesh.add_tree"
    bl_label = "Add Tree"
    bl_options = {"REGISTER", "UNDO"}
    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )
    
    generations = 3
    variations = 5
    
    verts = []
    root = []
    edges = []
    faces = []
    
    def get_all_paths(self,node,path=None):
        paths = []
        if path is None:
            path = []
        path.append(node)
        if node.childs:
            for child in node.childs:
                paths.extend(self.get_all_paths(child, path[:]))
        else:
            paths.append(path)
        return paths
    
    def build(self,x,y,z):
        self.root = TreeNode(x,y,z,self.variations,0)
        nodelist = []
        nodelist.append(self.root)
        while self.root.addChild(self.generations,nodelist) != 0:
            print("*")
        paths = self.get_all_paths(self.root)
        
        #print(paths)
            
        edgeIndex = 0
        edgePaths = []
        
        for node in nodelist:
            self.verts.append(node.vector)
            
        for edgePath in paths:
            for i in range(len(edgePath)):
                if 0 <= i+1 < len(edgePath):
                    edgepair = []
                    edgepair.append(edgePath[i].index)
                    edgepair.append(edgePath[i+1].index)
                    self.edges.append(edgepair)
        print(self.edges)
        print(self.verts)
                
        
        
    def execute(self, context):
        scale_x = self.scale.x
        scale_y = self.scale.y
        
        self.build(0,0,0)
                
        mesh = bpy.data.meshes.new(name="New Tree Mesh")
        mesh.from_pydata(self.verts, self.edges, self.faces)
        # useful for development when the mesh may be invalid.
        # mesh.validate(verbose=True)
        object_data_add(context, mesh, operator=self)
        return {'FINISHED'}

class TreeMainPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Procedural Tree"
    bl_idname = "panel.tree_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Procedural Tree'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        
        row.operator('mesh.add_tree',icon='MESH_CUBE', text="Add Tree")
        
        
def register():
    bpy.utils.register_class(TreeMainPanel)
    bpy.utils.register_class(Tree)


def unregister():
    bpy.utils.unregister_class(TreeMainPanel)
    bpy.utils.unregister_class(Tree)
    
if __name__ == "__main__":
    register()