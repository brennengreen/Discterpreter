# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis

# DATA TYPES:
INTEGER = 'INTEGER'
# OPERATIONS
PLUS, MINUS =  'PLUS', 'MINUS'
# FILE OPERATIONS
EOF = 'EOF'

operations = {'+':PLUS, '-':MINUS}

class Token(object):
	def __init__(self, type, value):
		# token type: INTEGER, PLUS, EOF
		self.type = type
		self.value = value

	def __str__(self):
		# String represenation of token		#
		# Example: Token(INTEGER, 3)		#
		#		   Token(PLUS, '+')			#
		return "Token({type}, {value})".format(
			type=self.type,
			value=self.value
		)
	
	def __repr__(self):
		return self.__str__()

class Interpreter(object):
	def __init__(self, text):
		# client string input, e.g. "3+5"
		self.text = text
		# self.pos is an index ingto self.text
		self.pos = 0
		# current token instance
		self.current_token = None
	
	def error(self):
		raise Exception("Error Parsing Input")
	
	def get_next_token(self):
		# Lexical Analyzer (aka Scanner/Tokenizer) #
		#                                          #
		# This method is responsible for breaking  #
		# breaking a sentence apart into token.    #
		text = self.text

		# Check if Interpreter is at end of input
		if self.pos > len(text) - 1:
			return Token(EOF, None)
		
		current_char = text[self.pos]

		if current_char == " ":
			self.pos += 1
			return self.get_next_token()

		if current_char.isdigit():
			token = Token(INTEGER, int(current_char))
			self.pos += 1
			return token
		
		if current_char in operations:
			token = Token(operations[current_char], current_char)
			self.pos += 1
			return token
		
		self.error()
	
	def eat(self, token_type):
		if self.current_token.type == token_type:
			self.current_token = self.get_next_token()
		else:
			self.error()

	def expr(self):
		"""expr -> INTEGER PLUS INTEGER"""
		self.current_token = self.get_next_token()

		left = []
		while self.current_token.type == INTEGER:
			left.append(self.current_token)
			self.eat(INTEGER)
		left = int(''.join([str(t.value) for t in left]))

		operation = self.current_token
		self.eat(operation.type)

		right = []
		while self.current_token.type == INTEGER:
			right.append(self.current_token)
			self.eat(INTEGER)
		right = int(''.join([str(t.value) for t in right]))

		if operation.type == PLUS:
			return left + right
		if operation.type == MINUS:
			return left - right