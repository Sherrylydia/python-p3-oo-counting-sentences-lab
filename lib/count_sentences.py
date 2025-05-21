import re

class MyString:
  pass
  def __init__(self, value=""):
        self._value = ""
        self.value = value  # use setter for validation

  @property
  def value(self):
        return self._value

  @value.setter
  def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val

  def is_sentence(self):
        return self.value.endswith(".")

  def is_question(self):
        return self.value.endswith("?")

  def is_exclamation(self):
        return self.value.endswith("!")

  def count_sentences(self):
        # Split based on sentence-ending punctuation and remove empty strings
        sentences = re.split(r'[.!?]', self.value)
        return len([s for s in sentences if s.strip()])

  def __str__(self):
        return self.value