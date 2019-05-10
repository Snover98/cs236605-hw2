from hw2.experiments import run_experiment


def main():
    exp1_1()
    exp1_2()
    exp1_3()
    # exp2()


def exp1_1():
    print("Running experiment 1.1")
    for K in [32, 64]:
        for L in [2, 4, 8, 16]:
            exp_name = f'exp1_1_K{K}_L{L}'
            print(f"CURRENT RUN: {exp_name}")
            run_experiment(run_name=exp_name, filters_per_layer=[K], layers_per_block=L, pool_every=L,
                           hidden_dims=[1024])


def exp1_2():
    print("Running experiment 1.2")
    for L in [2, 4, 8]:
        for K in [32, 64, 128, 258]:
            exp_name = f'exp1_2_L{L}_K{K}'
            run_experiment(run_name=exp_name, filters_per_layer=[K], layers_per_block=L, pool_every=L,
                           hidden_dims=[1024])


def exp1_3():
    print("Running experiment 1.3")
    K = [64, 128, 256]
    for L in [1, 2, 3, 4]:
        exp_name = f'exp1_3_L{L}_K{K[0]}-{K[1]}-{K[2]}'
        run_experiment(run_name=exp_name, filters_per_layer=[K], layers_per_block=L, pool_every=L, hidden_dims=[1024])


def exp2():
    print("Running experiment 2")
    K = [64, 128, 256, 512]
    for L in [1, 2, 3, 4]:
        exp_name = f'exp2_L{L}_K{K[0]}-{K[1]}-{K[2]}'
        run_experiment(run_name=exp_name, filters_per_layer=K, layers_per_block=L, ycn=True, hidden_dims=[1024], pool_every=L)


if __name__ == '__main__':
    main()
