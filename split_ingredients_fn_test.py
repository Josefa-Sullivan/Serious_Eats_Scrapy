import split_ingredients_fn 

import unittest

class TestSplitIngredientsFn(unittest.TestCase):

    def test_1(self):
        test_str1 = '1 cup plus 1 tablespoon (250ml) canola or vegetable oil, divided,6 boneless, skinless chicken thighs'
        expect_1 = ['1 cup plus 1 tablespoon (250ml) canola or vegetable oil, divided', '6 boneless, skinless chicken thighs']
        obs_1 = split_ingredients_fn.split_ingredients(test_str1)
        self.assertEqual(expect_1,obs_1)


    def test_2(self):
        test_str2 = '1 cup plus 1 tablespoon (250ml) canola or vegetable oil, divided'
        expect_2= ['1 cup plus 1 tablespoon (250ml) canola or vegetable oil, divided']
        obs_2 = split_ingredients_fn.split_ingredients(test_str2)
        self.assertEqual(expect_2,obs_2)

    def test_3(self):
        test_str3 = '1 cup plus 1 tablespoon (250ml) canola or vegetable oil, divided,6 boneless, skinless chicken thighs (about 2 1/4 pounds; 1kg total),kosher salt,1 1/2 pounds cajun-style andouille sausage'
        expect_3= ['1 cup plus 1 tablespoon (250ml) canola or vegetable oil, divided', '6 boneless, skinless chicken thighs (about 2 1/4 pounds; 1kg total)','kosher salt','1 1/2 pounds cajun-style andouille sausage']
        obs_3 = split_ingredients_fn.split_ingredients(test_str3)
        self.assertEqual(expect_3,obs_3)


if __name__ == '__main__':
    unittest.main()