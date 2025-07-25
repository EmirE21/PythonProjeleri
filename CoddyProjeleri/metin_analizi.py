def metin_analizi(metin):
  words = [word.strip('.()/"%') for word in metin.lower().split()]
  word_count = {}
  for word in words:
    word_count[word] = word_count.get(word, 0) + 1
  unique_count = len(set(words))
  repeated_count = [word for word, count in word_count.items() if count > 1]
  polindromes = [word for word in set(words) if word.replace(" ", "") == word.replace(" ", "")[::-1]]
  return {
      "unique_count": unique_count,
      "repeated_count": repeated_count,
      "polindromes": polindromes
  }