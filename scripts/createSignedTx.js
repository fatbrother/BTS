import Web3 from 'web3';
import contractJson from './build/ConcertTickets.json'; // ABI + bytecode

async function getSignedTx({
  rpcUrl,
  privateKey,
  eventName,
  totalTickets,
  startTime,
  endTime,
  whitelist
}) {
  const web3 = new Web3(rpcUrl);
  const account = web3.eth.accounts.privateKeyToAccount(privateKey);
  const Concert = new web3.eth.Contract(contractJson.abi);

  // 1) Build the deployment tx data
  const deployData = Concert.deploy({
    data: contractJson.bytecode,
    arguments: [eventName, totalTickets, startTime, endTime, whitelist]
  }).encodeABI();

  // 2) Create the raw Tx object
  const tx = {
    from: account.address,
    to: undefined,            // no `to` for contract creation
    data: deployData,
    gas: await web3.eth.estimateGas({ data: deployData }),
    nonce: await web3.eth.getTransactionCount(account.address)
  };

  // 3) Sign it
  const signed = await account.signTransaction(tx);

  // 4) Return the raw transaction hex (no '0x' prefix)
  return signed.rawTransaction.slice(2);
}

// USAGE:
(async () => {
  const signedTxHex = await getSignedTx({
    rpcUrl: 'http://127.0.0.1:8545',
    privateKey: '0xYOUR_PRIVATE_KEY',
    eventName: 'My Concert',
    totalTickets: 100,
    startTime: Math.floor(Date.now()/1000) + 3600,        // e.g. an hour from now
    endTime:   Math.floor(Date.now()/1000) + 7200,        // two hours from now
    whitelist: ['0xabc…', '0xdef…']                      // other user addresses
  });

  // Then call your Flask API:
  const res = await fetch('http://localhost:5000/holdEvent', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${yourJwtToken}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      signedTx: signedTxHex,
      eventName: 'My Concert',
      startTime: Math.floor(Date.now()/1000) + 3600,
      endTime:   Math.floor(Date.now()/1000) + 7200,
      totalTickets: 100
    })
  });
  console.log(await res.json());
})();
