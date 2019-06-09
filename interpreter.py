# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis

# DATA TYPES:
INTEGER = 'INTEGER'
# OPERATIONS
PLUS, MINUS, MULTIPLY, DIVIDE =  'PLUS', 'MINUS','MULTIPLY','DIVIDE'
# FILE OPERATIONS
EOF = 'EOF'

class Token(object):
	def __init__(self, type, value):
		# token type: INTEGER, PLUS, EOF
		self.type = type
		self.value = value

	def __str__(self):
		# String represenation of token		#
		# Example: Token(INTEGER, 3)		#
		#		   Token(PLUS, '+')	#
		return "Token({type}, {value})".format(
			type=self.type,
			value=repr(self.value)
		)
	
	def __repr__(self):
		return self.__str__()

class Interpreter(object):
	def __init__(self, text):
		print(text)
		# client string input, e.g. "3+5"
		self.text = text
		# self.pos is an index ingto self.text
		self.pos = 0
		# current token instance
		self.current_token = None
		self.current_char = self.text[self.pos]
	
	def error(self):
		raise Exception("Invalid syntax")
	
	def advance(self):
		""" Advance the 'pos' pointer and s et the 'current_char' variable. """
		self.pos += 1
		if self.pos > len(self.text) - 1:
			self.current_char = None
		else:
			self.current_char = self.text[self.pos]

	def skip_whitespace(self):
		while self.current_char is not None and self.current_char.isspace():
			self.advance()
	
	def integer(self):
		""" Return a (multidigit) integer consumed from the input. """
		result = ''
		while self.current_char is not None and self.current_char.isdigit():
			result += self.current_char
			self.advance()
		return int(result)

	def get_next_token(self):
		# Lexical Analyzer (aka Scanner/Tokenizer) #
		#                                          #
		# This method is responsible for breaking  #
		# breaking a sentence apart into token.    #
		while self.current_char is not None:
			if self.current_char.isspace():
				self.skip_whitespace()
				continue
			
			if self.current_char.isdigit():
				return Token(INTEGER, self.integer())

			if self.current_char == '+':
				self.advance()
				return Token(PLUS, '+')
			if self.current_char == '-':
				self.advance()
				return Token(MINUS, '-')
			
			self.error()
		return Token(EOF, None)
	
	def eat(self, token_type):
		if self.current_token.type == token_type:
			self.current_token = self.get_next_token()
		else:
			self.error()

	def term(self):
		""" RETURN an INTEGER token value """
		token = self.current_token
		self.eat(INTEGER)
		return token.value

	def expr(self):
		""" parse then interpret stream """
		self.current_token = self.get_next_token()

		result = self.term()
		while self.current_token.type in (PLUS, MINUS):
			token = self.current_token
			if token.type == PLUS:
				self.eat(PLUS)
				result = result + self.term()
			elif token.type == MINUS:
				self.eat(MINUS)
				result = result - self.term()
		return result