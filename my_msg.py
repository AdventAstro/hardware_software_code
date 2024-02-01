def my_msg(loop_type):
    print("\n##############")
    print("Running",loop_type,"loop")
    print("#################")


def main():
    my_msg("for")
    for_loop()
    my_msg("while")
    while_loop()


if __name__ == "__main__":
    main()
