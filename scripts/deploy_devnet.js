const {
    Connection,
    Keypair,
    PublicKey,
    LAMPORTS_PER_SOL,
    clusterApiUrl
} = require('@solana/web3.js');
const {
    createMint,
    getOrCreateAssociatedTokenAccount,
    mintTo,
    setAuthority,
    AuthorityType
} = require('@solana/spl-token');
const fs = require('fs');
const path = require('path');

const WALLET_PATH = path.join(__dirname, 'devnet_keypair.json');
const CONFIG_PATH = path.join(__dirname, '..', 'devnet_config.json');

// Parse CLI args
const args = process.argv.slice(2);
let recipientArg = null;
for (let i = 0; i < args.length; i++) {
    if (args[i] === '--recipient' && args[i + 1]) {
        recipientArg = args[i + 1];
    }
}

async function main() {
    console.log('\x1b[36m[*] Connecting to Solana Devnet RPC...\x1b[0m');
    const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');

    // 1. Load or Generate Keypair
    let payer;
    if (fs.existsSync(WALLET_PATH)) {
        const secretKey = Uint8Array.from(JSON.parse(fs.readFileSync(WALLET_PATH, 'utf-8')));
        payer = Keypair.fromSecretKey(secretKey);
    } else {
        payer = Keypair.generate();
        fs.writeFileSync(WALLET_PATH, JSON.stringify(Array.from(payer.secretKey)));
    }
    
    console.log(`\x1b[32m[✔] Deployer/Fee Payer Wallet:\x1b[0m \x1b[1m${payer.publicKey.toBase58()}\x1b[0m`);

    // 2. Check Balance
    let balance = await connection.getBalance(payer.publicKey);
    const solBalance = (balance / LAMPORTS_PER_SOL);
    console.log(`[*] Deployer Balance: \x1b[93m${solBalance.toFixed(4)} SOL\x1b[0m`);

    if (balance < 0.05 * LAMPORTS_PER_SOL) {
        console.log('\n' + '='.repeat(80));
        console.log('\x1b[33m[!] DEVNET SOL GEREKLİ (TAMAMEN ÜCRETSİZ - 0 TL)\x1b[0m');
        console.log(`Deployer adresine işlem ücreti için ~0.1 - 0.5 test SOL'u gerekiyor.`);
        console.log(`Lütfen tarayıcından şu adresi aç: \x1b[96mhttps://faucet.solana.com\x1b[0m`);
        console.log(`Ve bu adrese test SOL'u gönder:\n  👉 \x1b[92m\x1b[1m${payer.publicKey.toBase58()}\x1b[0m\n`);
        console.log(`Test SOL'u gelince komutu tekrar çalıştırman yeterli!`);
        console.log('='.repeat(80) + '\n');
        process.exit(1);
    }

    // 3. Determine Recipient (Default to Payer or Custom Phantom Public Key)
    let recipientPubkey = payer.publicKey;
    if (recipientArg) {
        try {
            recipientPubkey = new PublicKey(recipientArg);
            console.log(`\x1b[32m[✔] Recipient Phantom Wallet:\x1b[0m ${recipientPubkey.toBase58()}`);
        } catch (e) {
            console.log(`\x1b[31m[!] Invalid recipient address provided, defaulting to deployer.\x1b[0m`);
        }
    }

    // 4. Create SPL Token Mint ($DEAI)
    console.log('\x1b[36m[*] Initializing SPL Token Mint ($DEAI - 9 Decimals)...\x1b[0m');
    const mint = await createMint(
        connection,
        payer,
        payer.publicKey,       // Mint Authority
        payer.publicKey,       // Freeze Authority
        9                      // 9 Decimals
    );
    console.log(`\x1b[32m[✔] $DEAI Token Mint Created:\x1b[0m \x1b[1m\x1b[93m${mint.toBase58()}\x1b[0m`);

    // 5. Create Token Account & Mint 1,000,000 $DEAI
    console.log(`\x1b[36m[*] Creating Associated Token Account for: ${recipientPubkey.toBase58()}...\x1b[0m`);
    const tokenAccount = await getOrCreateAssociatedTokenAccount(
        connection,
        payer,
        mint,
        recipientPubkey
    );
    console.log(`\x1b[32m[✔] Token Account Address:\x1b[0m ${tokenAccount.address.toBase58()}`);

    const supply = 1000000n * 1000000000n; // 1,000,000 with 9 decimals
    console.log('\x1b[36m[*] Minting 1,000,000 $DEAI into Vault...\x1b[0m');
    await mintTo(
        connection,
        payer,
        mint,
        tokenAccount.address,
        payer,
        supply
    );
    console.log('\x1b[32m[✔] 1,000,000 $DEAI Minted Successfully!\x1b[0m');

    // 6. Revoke Mint Authority to lock supply forever
    console.log('\x1b[36m[*] Revoking Mint Authority (Enforcing 1,000,000 Hard Cap)...\x1b[0m');
    await setAuthority(
        connection,
        payer,
        mint,
        payer.publicKey,
        AuthorityType.MintTokens,
        null
    );
    console.log('\x1b[32m[✔] Mint Authority Revoked! Supply is permanently capped at 1,000,000.\x1b[0m');

    // Save configuration
    const config = {
        network: "devnet",
        rpc_url: "https://api.devnet.solana.com",
        mint_address: mint.toBase58(),
        recipient_wallet: recipientPubkey.toBase58(),
        token_account: tokenAccount.address.toBase58(),
        decimals: 9,
        max_supply: "1,000,000",
        explorer_url: `https://explorer.solana.com/address/${mint.toBase58()}?cluster=devnet`,
        created_at: new Date().toISOString()
    };
    fs.writeFileSync(CONFIG_PATH, JSON.stringify(config, null, 2));

    console.log('\n' + '='.repeat(80));
    console.log('\x1b[32m🎉 DECENTRALIZED AI ($DEAI) DEVNET BAŞARIYLA YAYINLANDI!\x1b[0m');
    console.log(`  • Token Adı:      DecentralizedAI ($DEAI)`);
    console.log(`  • Toplam Arz:     1,000,000 (Sabit & Kilitli)`);
    console.log(`  • Mint Adresi:    \x1b[93m${mint.toBase58()}\x1b[0m`);
    console.log(`  • Sahip Cüzdan:   \x1b[94m${recipientPubkey.toBase58()}\x1b[0m`);
    console.log(`  • Solana Explorer:\x1b[96mhttps://explorer.solana.com/address/${mint.toBase58()}?cluster=devnet\x1b[0m`);
    console.log('='.repeat(80) + '\n');
}

main().catch(err => {
    console.error('\x1b[31m[ERROR]\x1b[0m', err.message || err);
    process.exit(1);
});
