class NumberGuessingGame:
    """
    간단한 숫자 맞추기 게임 클래스
    """
    def __init__(self, secret_number=42):
        """
        게임 초기화
        
        Args:
            secret_number (int): 맞춰야 할 비밀 숫자
        """
        self.secret_number = secret_number
        self.attempts = 0
        self.is_game_over = False
    
    def make_guess(self, guess):
        """
        숫자 추측 시도
        
        Args:
            guess (int): 추측한 숫자
            
        Returns:
            str: 피드백 메시지
        """
        if self.is_game_over:
            return "게임이 이미 종료되었습니다. 새 게임을 시작하세요."
        
        self.attempts += 1
        
        if guess < self.secret_number:
            return "더 큰 숫자를 입력하세요!"
        elif guess > self.secret_number:
            return "더 작은 숫자를 입력하세요!"
        else:
            self.is_game_over = True
            return f"정답입니다! {self.attempts}번 만에 맞추셨습니다."
    
    def reset_game(self, new_secret_number=None):
        """
        게임 초기화
        
        Args:
            new_secret_number (int, optional): 새로운 비밀 숫자
        """
        if new_secret_number is not None:
            self.secret_number = new_secret_number
        self.attempts = 0
        self.is_game_over = False
        return "게임이 초기화되었습니다."


def play_game():
    """
    게임을 콘솔에서 실행하는 함수
    """
    print("숫자 맞추기 게임에 오신 것을 환영합니다!")
    print("1과 100 사이의 숫자를 맞춰보세요.")
    
    import random
    game = NumberGuessingGame(random.randint(1, 100))
    
    while not game.is_game_over:
        try:
            guess = int(input("추측한 숫자를 입력하세요: "))
            result = game.make_guess(guess)
            print(result)
        except ValueError:
            print("유효한 숫자를 입력하세요.")
    
    play_again = input("다시 플레이하시겠습니까? (y/n): ")
    if play_again.lower() == 'y':
        play_game()


if __name__ == "__main__":
    play_game()