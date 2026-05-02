# esse foi desgraçado
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
            words: str = sentence.split()
            discountSentence = []
            discountPercent: float = (100 - discount)/100

            for word in words:
                if word.startswith('$') and word[1:].isdigit():
                    price = float(word[1:]) * discountPercent
                    discountSentence.append(f"${price:.2f}")
                else:
                    discountSentence.append(word)
 
            return ' '.join(discountSentence)

