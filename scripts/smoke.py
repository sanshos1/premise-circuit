import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.types import TransactionStatus
R=Path(__file__).parents[1];env=(R.parents[3]/'accounts.env').read_text();address=json.loads((R/'deployment.json').read_text())['contractAddress']
def client(n):
 key=re.search(rf'^ACCOUNT_{n}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',env,re.M).group(1).strip();return create_client(chain=studionet,account=create_account(account_private_key=key))
def write(n,name,args):
 c=client(n);tx=c.write_contract(address=address,function_name=name,args=args);print(name+'_tx='+str(tx),flush=True);r=c.wait_for_transaction_receipt(transaction_hash=tx,status=TransactionStatus.FINALIZED,retries=180,interval=5000,full_transaction=True);leader=(r.get('consensus_data',{}).get('leader_receipt')or[{}])[0];assert r.get('result_name')=='MAJORITY_AGREE' and leader.get('execution_result')=='SUCCESS';return str(tx)
stamp=str(int(time.time()));cid='ROUTE-'+stamp;auditor=client(1).account.address;premises=['The east entrance is level and has no stairs','The automatic doorway provides at least 1.2 meters of clear width','The corridor remains firm and at least 1.2 meters wide','A wide security gate connects directly to the level corridor','The complete route preserves wheelchair access through screening'];edges=[[0,4],[1,4],[2,4],[3,4]];sources=['https://raw.githubusercontent.com/sanshos1/premise-circuit/main/evidence/record-a.md','https://cdn.jsdelivr.net/gh/sanshos1/premise-circuit@main/evidence/record-b.md'];txs={'open':write(3,'open_circuit',[cid,auditor,'Wheelchair route continuity',premises,edges]),'audit':write(1,'audit',[cid,sources])};state=client(3).read_contract(address=address,function_name='get_circuit',args=[cid]);assert state['state']=='VERIFIED' and all(x=='SUPPORTED' for x in state['node_states']);proof={'circuitId':cid,'transactions':txs,'state':state,'walletDisclosure':'Both evidence files and wallets are operator-controlled technical fixtures.'};(R/'evidence'/'live-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof,indent=2),flush=True)

