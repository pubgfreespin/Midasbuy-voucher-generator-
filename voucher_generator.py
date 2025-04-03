import random
import string
import time

def generate_voucher():
    """Generate a single 18-character mixed-case alphanumeric voucher"""
    charset = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choices(charset, k=18))

def generate_voucher_file(filename="vouchers.txt", count=10_000_000):
    """Generate vouchers in batches and save to file"""
    start_time = time.time()
    
    with open(filename, 'w') as f:
        batch_size = 100_000  # Adjust based on system memory
        for _ in range(count // batch_size):
            # Generate batch and write to file
            batch = [generate_voucher() + '\n' for _ in range(batch_size)]
            f.writelines(batch)
            
            # Progress tracking
            generated = (1 + _) * batch_size
            if _ % 10 == 0:
                print(f"Generated {generated:,} vouchers...")
        
        # Write remaining vouchers
        remaining = count % batch_size
        if remaining > 0:
            batch = [generate_voucher() + '\n' for _ in range(remaining)]
            f.writelines(batch)

    print(f"Successfully generated {count:,} vouchers in {time.time()-start_time:.2f} seconds")
    print(f"Saved to: {filename}")

if __name__ == "__main__":
    generate_voucher_file()
