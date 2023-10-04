# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, Sulfuras, Aged_brie, Backstage_passes, Conjured

my_classes = {
    "Sulfuras": Sulfuras,
    "Aged Brie": Aged_brie,
    "Backstage passes": Backstage_passes,
    "Conjured": Conjured,
    "Item": Item,
}

names = ["Sulfuras", "Aged Brie", "Backstage passes", "Conjured", "Item"]

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_item_1(self):
        items = [Item("name1", 1, 5)]
        gr = GildedRose(items)

        # [1, 5] ==> [0, 4] ==> [-1, 2]
        item = items[0]
        # Arrange
        original_sell_in = item.sell_in
        original_quality = item.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = item.sell_in
        new_quality = item.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality < original_quality
        assert new_quality == original_quality-1

        # Arrange
        original_sell_in = item.sell_in
        original_quality = item.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = item.sell_in
        new_quality = item.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality < original_quality
        assert new_quality == original_quality-2
    
    def test_item_2(self):
        # [1, 1] ==> [0, 0] ==> [-1, 0]
        items = [Item("name2", 1, 1)]
        gr = GildedRose(items)

        item = items[0]
        
        # Arrange
        original_sell_in = item.sell_in
        original_quality = item.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = item.sell_in
        new_quality = item.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality < original_quality
        assert new_quality == original_quality-1

        # Arrange
        original_sell_in = item.sell_in
        original_quality = item.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = item.sell_in
        new_quality = item.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality == original_quality

    def test_item_3(self):
        # [10, 50] ==> [9, 49]
        items = [Item("name3", 10, 50)]
        gr = GildedRose(items)

        item = items[0]
        
        # Arrange
        original_sell_in = item.sell_in
        original_quality = item.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = item.sell_in
        new_quality = item.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality < original_quality
        assert new_quality == original_quality-1

    def test_sulfuras_item(self):
        # 1. [5, 80] ==> [5, 80]
        # 2. [0, 80] ==> [0, 80]
        sulfuras_1 = my_classes[names[0]](5, 80)
        sulfuras_2 = my_classes[names[0]](0, 80)
        items = [sulfuras_1, sulfuras_2]
        gr = GildedRose(items)

        for item in items:
            # Arrange
            original_sell_in = item.sell_in
            original_quality = item.quality

            # Act
            gr.update_quality()

            # Assert
            new_sell_in = item.sell_in
            new_quality = item.quality

            assert new_sell_in == original_sell_in
            
            assert new_quality > 50
            assert new_quality == original_quality


    def test_Aged_Brie_item_1(self):
        # [5, 50] ==> [4, 50]
        aged_brie_1 = my_classes[names[1]](5, 50)
        items = [aged_brie_1]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = aged_brie_1.sell_in
        original_quality = aged_brie_1.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = aged_brie_1.sell_in
        new_quality = aged_brie_1.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality == original_quality

    def test_Aged_Brie_item_2(self):
        # [3, 49] ==> [2, 50]
        aged_brie_2 = my_classes[names[1]](3, 49)
        items = [aged_brie_2]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = aged_brie_2.sell_in
        original_quality = aged_brie_2.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = aged_brie_2.sell_in
        new_quality = aged_brie_2.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality > original_quality
        assert new_quality == original_quality+1

    def test_Aged_Brie_item_3(self):
        # [0, 20] ==> [-1, 22]
        aged_brie_3 = my_classes[names[1]](0, 20)
        items = [aged_brie_3]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = aged_brie_3.sell_in
        original_quality = aged_brie_3.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = aged_brie_3.sell_in
        new_quality = aged_brie_3.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality > original_quality
        assert new_quality == original_quality+2
    
    def test_Aged_Brie_item_4(self):
        # [0, 49] ==> [-1, 50]
        aged_brie_4 = my_classes[names[1]](0, 49)
        items = [aged_brie_4]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = aged_brie_4.sell_in
        original_quality = aged_brie_4.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = aged_brie_4.sell_in
        new_quality = aged_brie_4.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality > original_quality
        assert new_quality == original_quality+1

    def test_Backstage_passes_item_1(self):
        # [5, 50] ==> [4, 50]
        backstage_passes_1 = my_classes[names[2]](5, 50)
        items = [backstage_passes_1]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = backstage_passes_1.sell_in
        original_quality = backstage_passes_1.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = backstage_passes_1.sell_in
        new_quality = backstage_passes_1.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality == original_quality

    def test_Backstage_passes_item_2(self):
        # [11, 20] ==> [10, 21] ==> [9, 23] ==> [8, 25]
        backstage_passes_2 = my_classes[names[2]](11, 20)
        items = [backstage_passes_2]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = backstage_passes_2.sell_in
        original_quality = backstage_passes_2.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = backstage_passes_2.sell_in
        new_quality = backstage_passes_2.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality > original_quality
        assert new_quality == original_quality+1


        # Arrange
        original_sell_in = backstage_passes_2.sell_in
        original_quality = backstage_passes_2.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = backstage_passes_2.sell_in
        new_quality = backstage_passes_2.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality > original_quality
        assert new_quality == original_quality+2


        # Arrange
        original_sell_in = backstage_passes_2.sell_in
        original_quality = backstage_passes_2.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = backstage_passes_2.sell_in
        new_quality = backstage_passes_2.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality > original_quality
        assert new_quality == original_quality+2

    def test_Backstage_passes_item_3(self):
        # [5, 10] ==> [4, 13]
        backstage_passes_3 = my_classes[names[2]](5, 10)
        items = [backstage_passes_3]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = backstage_passes_3.sell_in
        original_quality = backstage_passes_3.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = backstage_passes_3.sell_in
        new_quality = backstage_passes_3.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality > original_quality
        assert new_quality == original_quality+3
    
    def test_Backstage_passes_item_4(self):
        # [11, 49] ==> [10, 50]
        backstage_passes_4 = my_classes[names[2]](11, 49)
        items = [backstage_passes_4]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = backstage_passes_4.sell_in
        original_quality = backstage_passes_4.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = backstage_passes_4.sell_in
        new_quality = backstage_passes_4.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality > original_quality
        assert new_quality == original_quality+1
    
    def test_Backstage_passes_item_5(self):
        # [5, 48] ==> [4, 50]
        backstage_passes_5 = my_classes[names[2]](5, 48)
        items = [backstage_passes_5]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = backstage_passes_5.sell_in
        original_quality = backstage_passes_5.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = backstage_passes_5.sell_in
        new_quality = backstage_passes_5.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality > original_quality
        assert new_quality == original_quality+2
    
    def test_Backstage_passes_item_6(self):
        # [0, 48] ==> [-1, 0]
        backstage_passes_6 = my_classes[names[2]](0, 48)
        items = [backstage_passes_6]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = backstage_passes_6.sell_in
        original_quality = backstage_passes_6.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = backstage_passes_6.sell_in
        new_quality = backstage_passes_6.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality < original_quality
        assert new_quality == original_quality - original_quality

    def test_Conjured_item_1(self):
        # [1, 7] ==> [0, 5] ==> [-1, 1]
        conjured_1 = my_classes[names[3]](1, 7)
        items = [conjured_1]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = conjured_1.sell_in
        original_quality = conjured_1.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = conjured_1.sell_in
        new_quality = conjured_1.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality < original_quality
        assert new_quality == original_quality - 2

        # Arrange
        original_sell_in = conjured_1.sell_in
        original_quality = conjured_1.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = conjured_1.sell_in
        new_quality = conjured_1.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality < original_quality
        assert new_quality == original_quality - 4

    def test_Conjured_item_2(self):
        # [1, 1] ==> [0, 0]
        conjured_2 = my_classes[names[3]](1, 1)
        items = [conjured_2]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = conjured_2.sell_in
        original_quality = conjured_2.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = conjured_2.sell_in
        new_quality = conjured_2.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality < original_quality
        assert new_quality == original_quality-1

    def test_Conjured_item_3(self):
        # [0, 1] ==> [-1, 0]
        conjured_3 = my_classes[names[3]](0, 1)
        items = [conjured_3]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = conjured_3.sell_in
        original_quality = conjured_3.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = conjured_3.sell_in
        new_quality = conjured_3.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality < original_quality
        assert new_quality == original_quality-1
    
    def test_Conjured_item_4(self):
        # [10, 49] ==> [10, 47]
        conjured_4 = my_classes[names[3]](10, 49)
        items = [conjured_4]
        gr = GildedRose(items)

        # Arrange
        original_sell_in = conjured_4.sell_in
        original_quality = conjured_4.quality
        # Act
        gr.update_quality()
        # Assert
        new_sell_in = conjured_4.sell_in
        new_quality = conjured_4.quality

        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in-1
        
        assert new_quality > -1
        assert new_quality < 51
        assert new_quality < original_quality
        assert new_quality == original_quality-2

if __name__ == '__main__':
    unittest.main()
