#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                return [Background("background.png", 2)]