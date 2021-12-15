# -*- coding: utf-8 -*-

import json
import tempfile
import os

import bpy


def many_objects_push_position_and_actions(context) -> tuple:
    """Записывает в файл положение и название анимационного экшена для всех выделенных объектов.
    Сохраняет данные в словарь по именам объектов.

    """
    pass

def push_position_and_action(context) -> tuple:
    """Записывает в файл положение и название анимационного экшена выделенного объекта. """

    ob=context.object
    loc=ob.location[:]
    rot=ob.rotation_euler[:]
    scl=ob.scale[:]
    
    action=None
    if ob.animation_data and ob.animation_data.action:
        action = ob.animation_data.action.name
    
    data={
    "loc": loc,
    "rot": rot,
    "scl": scl,
    "action": action
    }
   # print(data)
    
    with open(os.path.join(tempfile.gettempdir(), 'saving_object_data.json'), 'w') as f:
        json.dump(data, f, indent=4)
    
    return(True, "Ok!")


def push_child_offs(context) -> tuple:
    """Сохраняет в файл параметры **CHILD_OF** констрейнов **root** кости выделенного рига. """
    
    ob=context.object
    bpy.ops.object.mode_set(mode='POSE')
    pose_root=None
    if "root" in ob.pose.bones:
        pose_root=ob.pose.bones["root"]
    #(pose CHILD_OF)
    save_data=dict()
    if pose_root:
        for constr in pose_root.constraints:
            if constr.type=="CHILD_OF":
                save_data[constr.name]=dict()
                save_data[constr.name]['target']=constr.target.name
                save_data[constr.name]['subtarget']=constr.subtarget

    with open(os.path.join(tempfile.gettempdir(), 'saving_child_offs.json'), 'w') as f:
        json.dump(save_data, f, indent=4)
    
    return(True, "Ok!")


def pull_position_and_action(context) -> tuple:
    """Считывает из файла параметры положения и название анимационного экшена и применяет к 
    выделенному объекту. """
    
    ob=context.object
    
    path=os.path.join(tempfile.gettempdir(), 'saving_object_data.json')
    if not os.path.exists(path):
        return(False, "data file not found")
    
    with open(path, 'r') as f:
        data= json.load(f)
        
    print(data)
    
    ob.location=data["loc"]
    ob.rotation_euler=data["rot"]
    ob.scale=data["scl"]
    
    if data["action"] and data["action"] in bpy.data.actions:
        action = bpy.data.actions[data["action"]]
        if not ob.animation_data:
            ob.animation_data_create()
        ob.animation_data.action=action
  
    return(True, "Ok!")


def pull_position_to_edit_bone(context) -> tuple:
    """Считывает из файла параметры положения и применяет к 
    выделенной кости в режиме Edit Mode. """

    ob=context.object

    path=os.path.join(tempfile.gettempdir(), 'saving_object_data.json')
    if not os.path.exists(path):
        return(False, "data file not found")
    
    with open(path, 'r') as f:
        data= json.load(f)
        
    print(data)


    return(True, "Ok!")


def pull_child_offs(context) -> tuple:
    """Считывает из файла параметры **CHILD_OF** констрейнов и применяет к 
    **root** кости выделенного рига. """

    ob=context.object
    
    path=os.path.join(tempfile.gettempdir(), 'saving_child_offs.json')
    if not os.path.exists(path):
        return(False, "data file not found")
    
    with open(path, 'r') as f:
        data= json.load(f)
        
    print(data)

    bpy.ops.object.mode_set(mode='POSE')
    if "root" in ob.pose.bones:
        root=ob.pose.bones["root"]

        for c_name in data:
            constr=root.constraints.new("CHILD_OF")
            constr.name=c_name
            constr.target=bpy.data.objects[data[c_name]["target"]]
            constr.subtarget=data[c_name]["subtarget"]
            constr.influence=0

    return(True, "Ok!")