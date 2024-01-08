def get_input(n_barcodes) -> list:
    concentrations = []

    for i in range(n_barcodes):
        nanograms = input(f"What is the concentration of barcode {i+1}? (ng/μl)\n")
        concentrations.append(int(nanograms))
    return concentrations

def calculate_pool_volumes(concentrations: list, end_volume: int) -> dict:
    avg = sum(concentrations) / len(concentrations)
    avg_pool_volume = end_volume / len(concentrations)
    factors = [avg / i for i in concentrations]
    volumes = [round(avg_pool_volume * factors[i], 1) for i in range(len(factors))]
    return volumes
    

def main():
    barcodes = int(input("How many barcodes are you sequencing? (1-24)\n"))
    concentratrions = get_input(barcodes)
    volumes = calculate_pool_volumes(concentratrions, 75)

    print("\n\n\nvolumes to pool:\n\nBc\tVolume")
    for i, vol in enumerate(volumes):
        print(f'{i+1}\t{vol}')
    print(f"The total volume is {sum(volumes)}")
    
    



if __name__ == "__main__":
    main()