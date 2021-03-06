import unittest


from vanilla_neural_nets.recurrent_neural_network.training_data import WordLevelRNNTrainingDataBuilder, _RNNTrainingData
from helpers.prepare import Word2VecSkipGramTrainingDataBuilder, _Word2VecSkipGramTrainingData
from helpers.prepare import Word2VecCBOWTrainingDataBuilder, _Word2VecCBOWTrainingData


class TestWord2VecSkipGramDataPreparation(unittest.TestCase):

    CORPUS = 'the dog went to the store. it then chased me home.'

    VOCABULARY_SIZE_WHEREBY_NO_WORDS_REMOVED = SOME_LARGE_NUMBER = 100
    EXPECTED_X_TRAIN_WHEN_NO_WORDS_REMOVED = [[10, 9, 7, 10, 9, 7, 10, 9, 7, 10, 9, 7], [1, 5, 1, 5, 1, 5, 1, 5]]
    EXPECTED_Y_TRAIN_WHEN_NO_WORDS_REMOVED = [[7, 2, 10, 2, 10, 9, 9, 7, 6, 7, 6, 0], [4, 8, 8, 1, 5, 3, 3, 0]]

    VOCABULARY_SIZE_WHEREBY_SOME_WORDS_REMOVED = 4
    EXPECTED_X_TRAIN_WHEN_SOME_WORDS_REMOVED = [[1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2], [1, 1, 1, 1, 1, 1, 1, 1]]
    EXPECTED_Y_TRAIN_WHEN_SOME_WORDS_REMOVED = [[2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]

    def test_X_train_correctly_encoded_as_indices_when_no_words_removed(self):
        training_data = Word2VecSkipGramTrainingDataBuilder.build(
            corpus=self.CORPUS,
            vocabulary_size=self.VOCABULARY_SIZE_WHEREBY_NO_WORDS_REMOVED
        )

        self.assertEqual(training_data.X_train,
            self.EXPECTED_X_TRAIN_WHEN_NO_WORDS_REMOVED)

    def test_y_train_correctly_encoded_as_indices_when_no_words_removed(self):
        training_data = Word2VecSkipGramTrainingDataBuilder.build(
            corpus=self.CORPUS,
            vocabulary_size=self.VOCABULARY_SIZE_WHEREBY_NO_WORDS_REMOVED
        )

        self.assertEqual(training_data.y_train,
            self.EXPECTED_Y_TRAIN_WHEN_NO_WORDS_REMOVED)

    def test_X_train_correctly_encoded_as_indices_when_some_words_removed(self):
        training_data = Word2VecSkipGramTrainingDataBuilder.build(
            corpus=self.CORPUS,
            vocabulary_size=self.VOCABULARY_SIZE_WHEREBY_SOME_WORDS_REMOVED
        )

        self.assertEqual(training_data.X_train,
            self.EXPECTED_X_TRAIN_WHEN_SOME_WORDS_REMOVED)

    def test_y_train_correctly_encoded_as_indices_when_some_words_removed(self):
        training_data = Word2VecSkipGramTrainingDataBuilder.build(
            corpus=self.CORPUS,
            vocabulary_size=self.VOCABULARY_SIZE_WHEREBY_SOME_WORDS_REMOVED
        )

        self.assertEqual(training_data.y_train,
            self.EXPECTED_Y_TRAIN_WHEN_SOME_WORDS_REMOVED)

    def test_word2vec_training_data_builder_base_class_is_rnn_training_data_builder(self):
        self.assertEqual(Word2VecSkipGramTrainingDataBuilder().__class__.__base__, WordLevelRNNTrainingDataBuilder)

    def test_word2vec_training_data_base_class_is_rnn_training_data(self):
        dummy_word2vec_training_data_instance = _Word2VecSkipGramTrainingData(tokenized_corpus=[])
        self.assertEqual(dummy_word2vec_training_data_instance.__class__.__base__, _RNNTrainingData)


class TestWord2VecCBOWDataPreparation(unittest.TestCase):

    CORPUS = 'the dog went to the store. it then chased me home.'

    VOCABULARY_SIZE_WHEREBY_NO_WORDS_REMOVED = SOME_LARGE_NUMBER = 100
    EXPECTED_X_TRAIN_WHEN_NO_WORDS_REMOVED = [[[7, 2, 9, 7], [2, 10, 7, 6], [10, 9, 6, 0]], [[4, 8, 5, 3], [8, 1, 3, 0]]]
    EXPECTED_Y_TRAIN_WHEN_NO_WORDS_REMOVED = [[10, 9, 7], [1, 5]]

    VOCABULARY_SIZE_WHEREBY_SOME_WORDS_REMOVED = 4
    EXPECTED_X_TRAIN_WHEN_SOME_WORDS_REMOVED = [[[2, 1, 1, 2], [1, 1, 2, 1], [1, 1, 1, 0]], [[1, 1, 1, 1], [1, 1, 1, 0]]]
    EXPECTED_Y_TRAIN_WHEN_SOME_WORDS_REMOVED = [[1, 1, 2], [1, 1]]

    def test_X_train_correctly_encoded_as_indices_when_no_words_removed(self):
        training_data = Word2VecCBOWTrainingDataBuilder.build(
            corpus=self.CORPUS,
            vocabulary_size=self.VOCABULARY_SIZE_WHEREBY_NO_WORDS_REMOVED
        )

        self.assertEqual(training_data.X_train,
            self.EXPECTED_X_TRAIN_WHEN_NO_WORDS_REMOVED)

    def test_y_train_correctly_encoded_as_indices_when_no_words_removed(self):
        training_data = Word2VecCBOWTrainingDataBuilder.build(
            corpus=self.CORPUS,
            vocabulary_size=self.VOCABULARY_SIZE_WHEREBY_NO_WORDS_REMOVED
        )

        self.assertEqual(training_data.y_train,
            self.EXPECTED_Y_TRAIN_WHEN_NO_WORDS_REMOVED)

    def test_X_train_correctly_encoded_as_indices_when_some_words_removed(self):
        training_data = Word2VecCBOWTrainingDataBuilder.build(
            corpus=self.CORPUS,
            vocabulary_size=self.VOCABULARY_SIZE_WHEREBY_SOME_WORDS_REMOVED
        )

        self.assertEqual(training_data.X_train,
            self.EXPECTED_X_TRAIN_WHEN_SOME_WORDS_REMOVED)

    def test_y_train_correctly_encoded_as_indices_when_some_words_removed(self):
        training_data = Word2VecCBOWTrainingDataBuilder.build(
            corpus=self.CORPUS,
            vocabulary_size=self.VOCABULARY_SIZE_WHEREBY_SOME_WORDS_REMOVED
        )

        self.assertEqual(training_data.y_train,
            self.EXPECTED_Y_TRAIN_WHEN_SOME_WORDS_REMOVED)

    def test_word2vec_training_data_builder_base_class_is_rnn_training_data_builder(self):
        self.assertEqual(Word2VecCBOWTrainingDataBuilder().__class__.__base__, WordLevelRNNTrainingDataBuilder)

    def test_word2vec_training_data_base_class_is_rnn_training_data(self):
        dummy_word2vec_training_data_instance = _Word2VecCBOWTrainingData(tokenized_corpus=[])
        self.assertEqual(dummy_word2vec_training_data_instance.__class__.__base__, _RNNTrainingData)
