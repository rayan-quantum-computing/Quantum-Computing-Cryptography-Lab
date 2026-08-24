# Quantum Computing & Cryptography Lab

Self-study log. I am learning quantum computing and quantum cryptography on my own, without a supervisor.

## What is in here

Small exercises where I test one idea at a time, and small tools I try to build and actually finish. Every file opens with a header comment: the date, what I was testing, what I expected, and what actually came out. Attempts that failed stay in the repo. They are the ones I learn from.

## Projects

- **quantum_password.py**: a password generator that draws its randomness from quantum measurements instead of the predictable randomness an ordinary computer uses.
  Full write-up: https://rayan-quantum.hashnode.dev/

More projects will be added here as I finish them.

## Where I am now

- Single qubits, Hadamard gates, and measurement statistics.
- Built the quantum password generator above.
- Next: a one-time pad that encrypts a message with a quantum-generated key.

## Where I am going

- BB84: two people share a secret key using quantum particles; an eavesdropper is detected because measuring a particle changes it.
- B92: a simpler version of the same key-sharing idea.
- Quantum secret sharing: split a secret key among several people so none can recover it alone.
- Shor's algorithm: how factoring large numbers can break RSA, the encryption used today.

This is a long road, and I am aware of the distance.
