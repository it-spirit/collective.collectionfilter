# -*- coding: utf-8 -*-
from collective.collectionfilter.tiles import DictDataWrapper
from collective.collectionfilter.baseviews import BaseSortOnView
from collective.collectionfilter.interfaces import ICollectionFilterResultListSort  # noqa
from plone.supermodel.model import Schema
from plone.tiles.tile import PersistentTile
from zope.interface import implementer

import plone.api


class ISortOnTile(Schema, ICollectionFilterResultListSort):
    pass


@implementer(ISortOnTile)
class SortOnTile(PersistentTile, BaseSortOnView):

    @property
    def edit_url(self):
        if not plone.api.user.has_permission(
            'cmf.ModifyPortalContent',
            obj=self.context
        ):
            return None
        return self.url.replace('@@', '@@edit-tile/')

    @property
    def settings(self):
        return DictDataWrapper(self.data)

    @property
    def filter_id(self):
        return self.id

    @property
    def reload_url(self):
        return self.url
