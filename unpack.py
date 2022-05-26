from tokenizer import Token, tokenize
from structure import ForLoop
from structure import structure
from context import Context


def unpack_forLoop(tokens: list[Token], ctx=None):
    unpacked_tokens = []

    for token in tokens:
        if isinstance(token, Token):
            unpacked_tokens.append(token)
        elif isinstance(token, ForLoop):
            for _ in range(token.number.value):
                ctx.loop += 1
                unpacked_tokens.extend(unpack_forLoop(token.body, ctx))

    return unpacked_tokens


def unpack(tokens, ctx=None):
    return unpack_forLoop(tokens, ctx)


if __name__ == "__main__":
    print(unpack(structure(tokenize("3↹2{1↹{9}}5"))))
