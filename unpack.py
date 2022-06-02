from tokenizer import Token, tokenize, TokenType
from structure import ForLoop
from structure import structure
from context import Context


def unpack_forLoop(tokens: list[Token], ctx=None):
    unpacked_tokens = []

    for token in tokens:
        if isinstance(token, Token):
            unpacked_tokens.append(token)
        elif isinstance(token, ForLoop):
            counter = 1
            evaluated = unpack_forLoop(token.body, ctx)
            print("Eval", evaluated)
            evaluated_2 = []
            for _ in range(token.number.value):
                for token in evaluated:
                    if token.value == "n":
                        evaluated_2.append(Token(TokenType.NUMBER, counter))
                        counter += 1
                    else:
                        evaluated_2.append(token)
                unpacked_tokens.extend(evaluated_2)

    return unpacked_tokens


def unpack(tokens, ctx=None):
    print(tokens)
    print(unpack_forLoop(tokens, ctx))
    return unpack_forLoop(tokens, ctx)


if __name__ == "__main__":
    print(unpack(structure(tokenize("3↹2{1↹{9}}5"))))
