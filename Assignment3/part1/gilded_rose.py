# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Sulfuras(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in, quality)


class Aged_brie(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)


class Backstage_passes(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)


class Conjured(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Conjured", sell_in, quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Sulfuras never has to be sold or decreases in Quality
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            if item.name == "Aged Brie":
                # "Aged Brie" actually increases in Quality the older it gets, twice after sell-by date
                if item.sell_in < 1:
                    item.quality = item.quality + 2
                else:
                    item.quality = item.quality + 1
            elif(item.name == "Backstage passes to a TAFKAL80ETC concert"):
                # Backstage passes increase 1(days > 10), 2 (days <= 10), 3(days <= 5), ==0(after sell-by date)
                if item.sell_in < 1:
                    item.quality = 0
                elif item.sell_in < 6:
                    item.quality += 3
                elif item.sell_in < 11:
                    item.quality += 2
                else:
                    item.quality += 1  
            elif item.name == "Conjured":
                # "Conjured" items degrade in Quality twice as fast as normal items
                item.quality -= 2
                if item.sell_in < 1:
                    item.quality -= 2
            else:
                # other items degrade 1 before date, 2 after date
                if item.sell_in > 0:
                    item.quality -= 1
                else:
                    item.quality -= 2
            
            #  check quality within range
            if item.quality > 50:
                item.quality = 50
            if item.quality < 0:
                item.quality = 0
            item.sell_in -= 1
            