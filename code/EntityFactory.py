#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background


class EntityFactory:

    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level1Bg-{i}', position(0, 0)))


        pass
