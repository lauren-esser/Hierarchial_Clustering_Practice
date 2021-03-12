#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

class MediatorInterface(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'test_import_workflow') and
                callable(subclass.test_import_workflow) or
                NotImplemented)

    @abc.abstractmethod
    def test_import_workflow():
        """Test loading of packages"""
        raise NotImplementedError