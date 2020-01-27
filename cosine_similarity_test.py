import cosine_similarity_ingredients
import IPython
import unittest

class TestSplitIngredientsFn(unittest.TestCase):

    def test_1(self):
        test_str1 = 'chicken corn potato eggs'
        test_str2 = 'chicken milk rice'
        test_str3 = 'beef soy sauce eggs'
        result = cosine_similarity_ingredients.get_vectors(*[test_str1, test_str2, test_str3])
        self.assertEqual(result.shape, (3,9))

    def test_constructor(self):
        test_str1 = 'chicken corn potato eggs'
        test_str2 = 'chicken milk rice'
        test_str3 = 'beef soy sauce eggs'

        link2ingredient = {}
        link2ingredient['www.chicken.com'] = test_str1
        link2ingredient['www.chickenwing.com'] = test_str2
        link2ingredient['www.beef.com'] = test_str3

        ingredient_classifier = cosine_similarity_ingredients.IngredientClassifier(link2ingredient)

        self.assertEqual(ingredient_classifier.corpus_matrix.shape, (3,9))


    def test_query(self):
        test_str1 = 'chicken chicken chicken chicken corn potato eggs'
        test_str2 = 'chicken milk rice'
        test_str3 = 'beef soy sauce eggs'

        link2ingredient = {}
        link2ingredient['www.chicken.com'] = test_str1
        link2ingredient['www.chickenwing.com'] = test_str2
        link2ingredient['www.beef.com'] = test_str3

        ingredient_classifier = cosine_similarity_ingredients.IngredientClassifier(link2ingredient)


        query_link = ingredient_classifier.query('chicken corn')

        self.assertEqual(ingredient_classifier.query_vector.shape, (1,9))

        self.assertEqual(query_link, 'www.chicken.com')


    def test_invalid_query(self):
        test_str1 = 'chicken corn potato eggs'
        test_str2 = 'chicken milk rice'
        test_str3 = 'beef soy sauce eggs'

        link2ingredient = {}
        link2ingredient['www.chicken.com'] = test_str1
        link2ingredient['www.chickenwing.com'] = test_str2
        link2ingredient['www.beef.com'] = test_str3

        ingredient_classifier = cosine_similarity_ingredients.IngredientClassifier(link2ingredient)


        
        with self.assertRaises(Exception) as context:
            query_link = ingredient_classifier.query('zebra')

        self.assertTrue('Query not in corpus' == context.exception.args[0])

        


if __name__ == '__main__':
    unittest.main()