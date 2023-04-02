
// EMERALD
// vanilla->lotr
recipes.addShapeless(<lotr:item.emerald>, [<minecraft:emerald>, <minecraft:emerald>]);
recipes.addShapeless(<lotr:item.emerald> * 2, [<minecraft:emerald>, <minecraft:emerald>, <minecraft:emerald>, <minecraft:emerald>]);
recipes.addShapeless(<lotr:tile.blockGem:9>, [<minecraft:emerald_block>, <minecraft:emerald_block>]);
// lotr->vanilla
recipes.addShapeless(<minecraft:emerald> * 2, [<lotr:item.emerald>]);
recipes.addShapeless(<minecraft:emerald> * 4, [<lotr:item.emerald>, <lotr:item.emerald>]);
recipes.addShapeless(<minecraft:emerald_block> * 4, [<lotr:tile.blockGem:9>, <lotr:tile.blockGem:9>]);

// DIAMOND (same as emerald but with diamonds: lotr:item.diamond & lotr:tile.blockGem:5)
// vanilla->lotr
recipes.addShapeless(<lotr:item.diamond>, [<minecraft:diamond>, <minecraft:diamond>]);
recipes.addShapeless(<lotr:item.diamond> * 2, [<minecraft:diamond>, <minecraft:diamond>, <minecraft:diamond>, <minecraft:diamond>]);
recipes.addShapeless(<lotr:tile.blockGem:5>, [<minecraft:diamond_block>, <minecraft:diamond_block>]);
// lotr->vanilla
recipes.addShapeless(<minecraft:diamond> * 2, [<lotr:item.diamond>]);
recipes.addShapeless(<minecraft:diamond> * 4, [<lotr:item.diamond>, <lotr:item.diamond>]);
recipes.addShapeless(<minecraft:diamond_block> * 4, [<lotr:tile.blockGem:5>, <lotr:tile.blockGem:5>]);
