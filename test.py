# -*- coding: utf-8 -*-

'''
author:       Jimmy
contact:      234390130@qq.com
file:         test.py
time:         2018/3/16 下午7:20
description: 

'''

__author__ = 'Jimmy'

import requests
import json
import utils.etc as  etc
import datetime as dt

# import eyed3
# import os
#
# file_path = os.path.join('www/static/sounds', '10049.mp3')
# audiofile = eyed3.load(file_path)
# print(u'时长为：{}秒'.format(audiofile.info.time_secs))

# r = requests.get('http://localhost:8888/blocks')
# print(json.loads(r.text))

from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

config = {
  "bytecode": "0x60806040526040805190810160405280600281526020017f4a420000000000000000000000000000000000000000000000000000000000008152506004908051906020019062000051929190620001b1565b506040805190810160405280600281526020017f4a42000000000000000000000000000000000000000000000000000000000000815250600590805190602001906200009f929190620001b1565b506004600660006101000a81548160ff021916908360ff1602179055506548c2739500006007556001600a60006101000a81548160ff0219169083151502179055506001600b5569043c33c1937564800000600c5569043c33c1937564800000600d556000600e5562030d40600f553480156200011b57600080fd5b5060075460018190555033600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506007546000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555062000260565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10620001f457805160ff191683800117855562000225565b8280016001018555821562000225579182015b828111156200022457825182559160200191906001019062000207565b5b50905062000234919062000238565b5090565b6200025d91905b80821115620002595760008160009055506001016200023f565b5090565b90565b612e4480620002706000396000f3006080604052600436106101b7576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063068b73101461060557806306fdde0314610630578063095ea7b3146106c05780630b7ddd251461072557806310f1a2741461076a57806312065fe0146107af57806318160ddd146107da5780631e89d5451461080557806323b872dd146108c65780632e1a7d4d1461094b5780632ff2e9dc14610990578063313ce567146109bb57806341c0e1b5146109ec5780635b22bbd214610a035780636618846314610a2e57806370a0823114610a9357806376db7fd414610aea57806379c6506814610b315780638f28397014610b9657806395d89b4114610bf15780639a70855e14610c81578063a899e61514610cb0578063a9059cbb14610cdb578063addd702014610d40578063b414d4b614610d6b578063c59ee1dc14610dc6578063c8d90df814610df1578063cd27d1a014610e48578063d73dd62314610e8d578063dd62ed3e14610ef2578063e2ece62114610f69578063e4b50ee814610fce578063e724529c14611013578063e8928f7a1461107a578063f851a440146110bf575b600080600080341115156101ca57600080fd5b600a60009054906101000a900460ff16156105b857600b5434101580156101f35750600c543411155b1561056b57600d54600e5410156105665734925061021c34600e5461111690919063ffffffff16565b600e81905550600d54600e5411156102ad57610245600d54600e5461113290919063ffffffff16565b915061025a823461113290919063ffffffff16565b92503373ffffffffffffffffffffffffffffffffffffffff166108fc839081150290604051600060405180830381858888f193505050501580156102a2573d6000803e3d6000fd5b50600d54600e819055505b600d54600e541015156102d6576000600a60006101000a81548160ff0219169083151502179055505b610303600f546102f5655af3107a40008661114b90919063ffffffff16565b61116190919063ffffffff16565b9050600080600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054811115151561037457600080fd5b6103e781600080600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461113290919063ffffffff16565b600080600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555061049c816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461111690919063ffffffff16565b6000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055503373ffffffffffffffffffffffffffffffffffffffff16600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a35b6105b3565b3373ffffffffffffffffffffffffffffffffffffffff166108fc349081150290604051600060405180830381858888f193505050501580156105b1573d6000803e3d6000fd5b505b610600565b3373ffffffffffffffffffffffffffffffffffffffff166108fc349081150290604051600060405180830381858888f193505050501580156105fe573d6000803e3d6000fd5b505b505050005b34801561061157600080fd5b5061061a611199565b6040518082815260200191505060405180910390f35b34801561063c57600080fd5b5061064561119f565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561068557808201518184015260208101905061066a565b50505050905090810190601f1680156106b25780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156106cc57600080fd5b5061070b600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019092919050505061123d565b604051808215151515815260200191505060405180910390f35b34801561073157600080fd5b506107506004803603810190808035906020019092919050505061137c565b604051808215151515815260200191505060405180910390f35b34801561077657600080fd5b50610795600480360381019080803590602001909291905050506113ea565b604051808215151515815260200191505060405180910390f35b3480156107bb57600080fd5b506107c4611458565b6040518082815260200191505060405180910390f35b3480156107e657600080fd5b506107ef611477565b6040518082815260200191505060405180910390f35b34801561081157600080fd5b506108ac6004803603810190808035906020019082018035906020019080806020026020016040519081016040528093929190818152602001838360200280828437820191505050505050919291929080359060200190820180359060200190808060200260200160405190810160405280939291908181526020018383602002808284378201915050505050509192919290505050611481565b604051808215151515815260200191505060405180910390f35b3480156108d257600080fd5b50610931600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050611855565b604051808215151515815260200191505060405180910390f35b34801561095757600080fd5b5061097660048036038101908080359060200190929190505050611cb6565b604051808215151515815260200191505060405180910390f35b34801561099c57600080fd5b506109a5611d64565b6040518082815260200191505060405180910390f35b3480156109c757600080fd5b506109d0611d6a565b604051808260ff1660ff16815260200191505060405180910390f35b3480156109f857600080fd5b50610a01611d7d565b005b348015610a0f57600080fd5b50610a18611e14565b6040518082815260200191505060405180910390f35b348015610a3a57600080fd5b50610a79600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050611e1a565b604051808215151515815260200191505060405180910390f35b348015610a9f57600080fd5b50610ad4600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506120fe565b6040518082815260200191505060405180910390f35b348015610af657600080fd5b50610b17600480360381019080803515159060200190929190505050612146565b604051808215151515815260200191505060405180910390f35b348015610b3d57600080fd5b50610b7c600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803590602001909291905050506121c7565b604051808215151515815260200191505060405180910390f35b348015610ba257600080fd5b50610bd7600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506122e6565b604051808215151515815260200191505060405180910390f35b348015610bfd57600080fd5b50610c06612523565b6040518080602001828103825283818151815260200191508051906020019080838360005b83811015610c46578082015181840152602081019050610c2b565b50505050905090810190601f168015610c735780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b348015610c8d57600080fd5b50610c966125c1565b604051808215151515815260200191505060405180910390f35b348015610cbc57600080fd5b50610cc56125d4565b6040518082815260200191505060405180910390f35b348015610ce757600080fd5b50610d26600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803590602001909291905050506125da565b604051808215151515815260200191505060405180910390f35b348015610d4c57600080fd5b50610d556128a0565b6040518082815260200191505060405180910390f35b348015610d7757600080fd5b50610dac600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506128a6565b604051808215151515815260200191505060405180910390f35b348015610dd257600080fd5b50610ddb6128c6565b6040518082815260200191505060405180910390f35b348015610dfd57600080fd5b50610e32600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506128cc565b6040518082815260200191505060405180910390f35b348015610e5457600080fd5b50610e73600480360381019080803590602001909291905050506128e4565b604051808215151515815260200191505060405180910390f35b348015610e9957600080fd5b50610ed8600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050612952565b604051808215151515815260200191505060405180910390f35b348015610efe57600080fd5b50610f53600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050612b24565b6040518082815260200191505060405180910390f35b348015610f7557600080fd5b50610fb4600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050612bab565b604051808215151515815260200191505060405180910390f35b348015610fda57600080fd5b50610ff960048036038101908080359060200190929190505050612c57565b604051808215151515815260200191505060405180910390f35b34801561101f57600080fd5b50611060600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803515159060200190929190505050612cc5565b604051808215151515815260200191505060405180910390f35b34801561108657600080fd5b506110a560048036038101908080359060200190929190505050612d84565b604051808215151515815260200191505060405180910390f35b3480156110cb57600080fd5b506110d4612df2565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6000818301905082811015151561112957fe5b80905092915050565b600082821115151561114057fe5b818303905092915050565b6000818381151561115857fe5b04905092915050565b6000808314156111745760009050611193565b818302905081838281151561118557fe5b0414151561118f57fe5b8090505b92915050565b600c5481565b60048054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156112355780601f1061120a57610100808354040283529160200191611235565b820191906000526020600020905b81548152906001019060200180831161121857829003601f168201915b505050505081565b60008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054821115151561128c57600080fd5b81600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925846040518082815260200191505060405180910390a36001905092915050565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156113da57600080fd5b81600e8190555060019050919050565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561144857600080fd5b81600b8190555060019050919050565b60003073ffffffffffffffffffffffffffffffffffffffff1631905090565b6000600154905090565b600080600080600080600860003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff161515156114e357600080fd5b600960003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020544211151561153057600080fd5b8651885114151561154057600080fd5b8751945060008511151561155357600080fd5b60009350600092505b848310156115ab5761158e878481518110151561157557fe5b906020019060200201518561111690919063ffffffff16565b93506115a460018461111690919063ffffffff16565b925061155c565b6000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205484111515156115f857600080fd5b600091505b8482101561184657878281518110151561161357fe5b906020019060200201519050600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415151561165b57600080fd5b6116c3878381518110151561166c57fe5b906020019060200201516000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461111690919063ffffffff16565b6000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555061176d878381518110151561171657fe5b906020019060200201516000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461113290919063ffffffff16565b6000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508073ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef898581518110151561180c57fe5b906020019060200201516040518082815260200191505060405180910390a361183f60018361111690919063ffffffff16565b91506115fd565b60019550505050505092915050565b6000600860008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff161515156118b057600080fd5b600960003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054421115156118fd57600080fd5b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff161415151561193957600080fd5b6000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054821115151561198657600080fd5b600260008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020548211151515611a1157600080fd5b611a62826000808773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461113290919063ffffffff16565b6000808673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550611af5826000808673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461111690919063ffffffff16565b6000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550611bc682600260008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461113290919063ffffffff16565b600260008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a3600190509392505050565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515611d1457600080fd5b3373ffffffffffffffffffffffffffffffffffffffff166108fc839081150290604051600060405180830381858888f19350505050158015611d5a573d6000803e3d6000fd5b5060019050919050565b60075481565b600660009054906101000a900460ff1681565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515611dd957600080fd5b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16ff5b600d5481565b6000806000600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054915081841115611f2d576000600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550612011565b611f40848361113290919063ffffffff16565b90506000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020548111151515611f8f57600080fd5b80600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055505b8473ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008973ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020546040518082815260200191505060405180910390a360019250505092915050565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156121a457600080fd5b81600a60006101000a81548160ff02191690831515021790555060019050919050565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561222557600080fd5b612276826000808673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461111690919063ffffffff16565b6000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055506122cd8260015461111690919063ffffffff16565b6001819055506001546007819055506001905092915050565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561234457600080fd5b600073ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415151561238057600080fd5b612431600080600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020546000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461111690919063ffffffff16565b6000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055506000806000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555081600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060019050919050565b60058054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156125b95780601f1061258e576101008083540402835291602001916125b9565b820191906000526020600020905b81548152906001019060200180831161259c57829003601f168201915b505050505081565b600a60009054906101000a900460ff1681565b600f5481565b6000600860003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff1615151561263557600080fd5b600960003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020544211151561268257600080fd5b600073ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff16141515156126be57600080fd5b6000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054821115151561270b57600080fd5b61275c826000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461113290919063ffffffff16565b6000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055506127ef826000808673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461111690919063ffffffff16565b6000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a36001905092915050565b600b5481565b60086020528060005260406000206000915054906101000a900460ff1681565b600e5481565b60096020528060005260406000206000915090505481565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561294257600080fd5b81600d8190555060019050919050565b6000806129e483600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205461111690919063ffffffff16565b90506000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020548111151515612a3357600080fd5b80600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508373ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925836040518082815260200191505060405180910390a3600191505092915050565b6000600260008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054905092915050565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515612c0957600080fd5b81600960008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055506001905092915050565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515612cb557600080fd5b81600f8190555060019050919050565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515612d2357600080fd5b81600860008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055506001905092915050565b6000600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515612de257600080fd5b81600c8190555060019050919050565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16815600a165627a7a72305820d89508cbb563c35d5ceff5e43e65ffc715b7dc1a5dcf7ef4755530f4e5bfd7bd0029",
  "abi": [
    {
      "constant": True,
      "inputs": [],
      "name": "maxWei",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "name",
      "outputs": [
        {
          "name": "",
          "type": "string"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "totalSupply",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "INITIAL_SUPPLY",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "decimals",
      "outputs": [
        {
          "name": "",
          "type": "uint8"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "maxRaiseAmount",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_owner",
          "type": "address"
        }
      ],
      "name": "balanceOf",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "symbol",
      "outputs": [
        {
          "name": "",
          "type": "string"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "exchangeFlag",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "raiseRatio",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "minWei",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "frozenAccount",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "raisedAmount",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "name": "frozenTimestamp",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_owner",
          "type": "address"
        },
        {
          "name": "_spender",
          "type": "address"
        }
      ],
      "name": "allowance",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "admin",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "payable": True,
      "stateMutability": "payable",
      "type": "fallback"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "name": "spender",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Approval",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "from",
          "type": "address"
        },
        {
          "indexed": True,
          "name": "to",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Transfer",
      "type": "event"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_newAdmin",
          "type": "address"
        }
      ],
      "name": "changeAdmin",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_target",
          "type": "address"
        },
        {
          "name": "_amount",
          "type": "uint256"
        }
      ],
      "name": "generateToken",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_amount",
          "type": "uint256"
        }
      ],
      "name": "withdraw",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_target",
          "type": "address"
        },
        {
          "name": "_freeze",
          "type": "bool"
        }
      ],
      "name": "freeze",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_target",
          "type": "address"
        },
        {
          "name": "_timestamp",
          "type": "uint256"
        }
      ],
      "name": "freezeWithTimestamp",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_targets",
          "type": "address[]"
        },
        {
          "name": "_freezes",
          "type": "bool[]"
        }
      ],
      "name": "multiFreeze",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_targets",
          "type": "address[]"
        },
        {
          "name": "_timestamps",
          "type": "uint256[]"
        }
      ],
      "name": "multiFreezeWithTimestamp",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_tos",
          "type": "address[]"
        },
        {
          "name": "_values",
          "type": "uint256[]"
        }
      ],
      "name": "multiTransfer",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_to",
          "type": "address"
        },
        {
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "transfer",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_from",
          "type": "address"
        },
        {
          "name": "_to",
          "type": "address"
        },
        {
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "transferFrom",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_spender",
          "type": "address"
        },
        {
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "approve",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_spender",
          "type": "address"
        },
        {
          "name": "_addedValue",
          "type": "uint256"
        }
      ],
      "name": "increaseApproval",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_spender",
          "type": "address"
        },
        {
          "name": "_subtractedValue",
          "type": "uint256"
        }
      ],
      "name": "decreaseApproval",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_target",
          "type": "address"
        }
      ],
      "name": "getFrozenTimestamp",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_target",
          "type": "address"
        }
      ],
      "name": "getFrozenAccount",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "getBalance",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_value",
          "type": "string"
        }
      ],
      "name": "setName",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_value",
          "type": "string"
        }
      ],
      "name": "setSymbol",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_flag",
          "type": "bool"
        }
      ],
      "name": "setExchangeFlag",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "setMinWei",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "setMaxWei",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "setMaxRaiseAmount",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "setRaisedAmount",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_value",
          "type": "uint256"
        }
      ],
      "name": "setRaiseRatio",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [],
      "name": "kill",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ],
  "address": "0x345ca3e014aaf5dca488057592ee47305d9b3e10",
}
web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
owner = web3.eth.accounts[0]
print(owner)
user1 = web3.eth.accounts[1]
user2 = web3.eth.accounts[2]
user3 = web3.eth.accounts[3]
user4 = web3.eth.accounts[4]
user5 = web3.eth.accounts[5]
user6 = web3.eth.accounts[6]

print(web3.fromWei(20000000000000000000000,'ether'))

# ul = web3.personal.unlockAccount(owner, '123456')
# print(ul)

# ct = web3.eth.contract(abi=config['abi'], bytecode=config['bytecode'])
# egas = ct.constructor().estimateGas()
# print(egas)
#
# tx_hash = ct.constructor().transact({'from': owner, 'gas': 4000000, 'gasPrice':2000000000, 'nonce':0})
# tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash,9999999999999)
# print(tx_receipt)

# tx = web3.eth.sendTransaction({
#   'to': Web3.toChecksumAddress(config['address']),
#   'from': user1,
#   'value': 1000000000000000,
#   'gas': 200000,
#   'gasPrice':10000000000
#   }
# )
#
# tx = web3.eth.sendTransaction({
#   'to': Web3.toChecksumAddress(config['address']),
#   'from': user2,
#   'value': 1500000000000000000,
#   'gas': 200000,
#   'gasPrice':10000000000
#   }
# )
# tx = web3.eth.sendTransaction({
#   'to': Web3.toChecksumAddress(config['address']),
#   'from': user3,
#   'value': 10000000000000000,
#   'gas': 200000,
#   'gasPrice':10000000000
#   }
# )
#
# tx = web3.eth.sendTransaction({
#   'to': Web3.toChecksumAddress(config['address']),
#   'from': user4,
#   'value': 15000000000000000000,
#   'gas': 200000,
#   'gasPrice':10000000000
#   }
# )
#
# tx = web3.eth.sendTransaction({
#   'to': Web3.toChecksumAddress(config['address']),
#   'from': user5,
#   'value': 23200000000000000000,
#   'gas': 200000,
#   'gasPrice':10000000000
#   }
# )

# ci = web3.eth.contract(address=Web3.toChecksumAddress(config['address']),
#                                           abi=config['abi'],
#                                           ContractFactoryClass=ConciseContract)

# print(ci.getFrozenAccount(user1))
# print(ci.getFrozenAccount(user2))
# print(ci.getFrozenTimestamp(user3))
# print(ci.getFrozenTimestamp(user4))

# ci.generateToken(owner,1000000000000000000000000000, transact={'from': user1, 'gas': 200000, 'gasPrice':2000000000})

# ci.freeze(user1, False, transact={'from': user1, 'gas': 200000, 'gasPrice':2000000000})
# ci.multiFreeze([user1,user2],[True, True],transact={'from': owner, 'gas': 200000, 'gasPrice':2000000000})
# ci.multiFreezeWithTimestamp([user3,user4],[1529479800, 1529479800],transact={'from': owner, 'gas': 200000, 'gasPrice':2000000000})

# print(ci.frozenTimestamp(user3))

# ci.kill(transact={'from': owner})
# ci.setExchangeFlag(True, transact={'from': owner})
# ci.setMaxRaiseAmount(200000000000000000000, transact={'from': owner})
# tx_hash = ci.setRaiseRatio(10000000, transact={'from': owner, 'gas': 200000, 'gasPrice':2000000000, 'nonce':1})
# tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash,9999999999999)
# print(tx_receipt)


# ci.withdraw(100000000000000000000, transact={'from': owner})

# print(ci.exchangeFlag())
# print(web3.fromWei(ci.getBalance(),'ether'))
# print(ci.raisedAmount())


# ci.decreaseApproval(user3, 1000000000000, transact={'from': user4})

# ci.transferFrom(user4, user0, 2000000000000, transact={'from': user3})

# ci.transfer(user3, 10000000000000000000, transact={'from': user4, 'gas': 4000000, 'gasPrice':1000000000})

# ci.transfer(user3, 1000000000000, transact={'from': user4})

# ci.freezeAccountWithTimestamp(user3, 1528867380, transact={'from': owner})

# ci.multiTransfer([user0, user2, user3, user4],[10000000000000,10000000000000,10000000000000,10000000000000], transact={'from': owner})


# tx = ci.changeAdmin(owner, transact={'from': user1})
# print(tx)
# owerb = ci.balanceOf(owner)
# print(web3.fromWei(owerb,'ether'))
# owerb = ci.balanceOf(user1)
# print(web3.fromWei(owerb,'ether'))
# owerb = ci.balanceOf(user2)
# print(web3.fromWei(owerb,'ether'))
# owerb = ci.balanceOf(user3)
# print(web3.fromWei(owerb,'ether'))
# owerb = ci.balanceOf(user4)
# print(web3.fromWei(owerb,'ether'))
# owerb = ci.balanceOf(user5)
# print(web3.fromWei(owerb,'ether'))
# owerb = ci.balanceOf(user6)
# print(owerb)
# owerb = ci.allowance(user4, user3)
# print(owerb)
# tx = ci.mintToken(owner, 10000000000000, transact={'from': user1})
# print(tx)
# owerb = ci.balanceOf(owner)
# print(owerb)