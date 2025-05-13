import unittest
from game import NumberGuessingGame

class TestNumberGuessingGame(unittest.TestCase):
    """
    숫자 맞추기 게임 테스트 클래스
    """
    
    def setUp(self):
        """
        각 테스트 전에 실행되는 설정
        """
        self.game = NumberGuessingGame(42)
    
    def test_initialization(self):
        """
        게임 초기화 테스트
        """
        self.assertEqual(self.game.secret_number, 42)
        self.assertEqual(self.game.attempts, 0)
        self.assertFalse(self.game.is_game_over)
    
    def test_correct_guess(self):
        """
        정답을 맞추었을 때 테스트
        """
        result = self.game.make_guess(42)
        self.assertTrue(self.game.is_game_over)
        self.assertEqual(self.game.attempts, 1)
        self.assertTrue("정답입니다" in result)
    
    def test_too_low_guess(self):
        """
        추측한 숫자가 정답보다 작을 때 테스트
        """
        result = self.game.make_guess(30)
        self.assertFalse(self.game.is_game_over)
        self.assertEqual(self.game.attempts, 1)
        self.assertTrue("더 큰 숫자" in result)
    
    def test_too_high_guess(self):
        """
        추측한 숫자가 정답보다 클 때 테스트
        """
        result = self.game.make_guess(50)
        self.assertFalse(self.game.is_game_over)
        self.assertEqual(self.game.attempts, 1)
        self.assertTrue("더 작은 숫자" in result)
    
    def test_multiple_guesses(self):
        """
        여러 번 추측했을 때 테스트
        """
        self.game.make_guess(10)
        self.game.make_guess(30)
        result = self.game.make_guess(42)
        self.assertTrue(self.game.is_game_over)
        self.assertEqual(self.game.attempts, 3)
        self.assertTrue("3번" in result)
    
    def test_game_over(self):
        """
        게임이 종료된 후 추가 시도 테스트
        """
        self.game.make_guess(42)  # 게임 종료
        result = self.game.make_guess(42)
        self.assertTrue("이미 종료" in result)
        self.assertEqual(self.game.attempts, 1)  # 시도 횟수 증가하지 않음
    
    def test_reset_game(self):
        """
        게임 초기화 테스트
        """
        self.game.make_guess(30)
        self.game.make_guess(42)
        self.game.reset_game()
        self.assertEqual(self.game.attempts, 0)
        self.assertFalse(self.game.is_game_over)
        self.assertEqual(self.game.secret_number, 42)
    
    def test_reset_game_with_new_number(self):
        """
        새로운 숫자로 게임 초기화 테스트
        """
        self.game.reset_game(100)
        self.assertEqual(self.game.secret_number, 100)
        self.assertEqual(self.game.attempts, 0)
        self.assertFalse(self.game.is_game_over)


if __name__ == "__main__":
    unittest.main()