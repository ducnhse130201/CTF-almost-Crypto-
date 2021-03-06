#!/usr/bin/python
# -*- coding: utf-8 -*-

import struct
import os
import hashlib
import binascii

tbl = [
    [0xd, 0x12, 0x19, 0x15, 0x9c, 0x5, 0x1, 0xab, 0x5e, 0x6f, 0x9, 0x45,
     0x90, 0xb9, 0xc5, 0x18, 0xa4, 0xec, 0xa7, 0x13, 0x94, 0x37, 0x29, 0x9e,
     0xc3, 0xba, 0xcc, 0xc1, 0xf2, 0xca, 0x1c, 0xae, 0xd9, 0x93, 0xfd, 0x48,
     0x58, 0x51, 0x99, 0xa2, 0x5a, 0xcb, 0x8b, 0x9f, 0x1f, 0xb6, 0x5f, 0x7b,
     0x6a, 0xa9, 0x4d, 0xad, 0x76, 0xf8, 0x6b, 0xf4, 0x69, 0x7c, 0xee, 0x8c,
     0x85, 0x49, 0xdc, 0x1b, 0x67, 0xed, 0x42, 0x74, 0x75, 0x0, 0x34, 0xce,
     0x3c, 0x55, 0xb8, 0xdd, 0x47, 0x8d, 0x41, 0xea, 0x3d, 0xbf, 0x6e, 0x83,
     0x4e, 0x92, 0xdf, 0x35, 0x4, 0xa5, 0xd0, 0x57, 0x24, 0x22, 0x36, 0xa1,
     0xbe, 0x81, 0xc4, 0x95, 0x2d, 0x23, 0x5d, 0xeb, 0x2b, 0x97, 0x6c, 0x11,
     0x3e, 0x52, 0xf1, 0xc6, 0x3f, 0xcd, 0x2e, 0xe1, 0xfc, 0xf3, 0x56, 0x9b,
     0xd2, 0xd8, 0xb4, 0x4f, 0x7e, 0x91, 0x9d, 0xbc, 0xa3, 0x62, 0x7d, 0x82,
     0x31, 0xf9, 0x2a, 0x79, 0xaa, 0xc9, 0x10, 0x53, 0xa, 0x33, 0x77, 0x1d,
     0xe, 0xef, 0x21, 0xb2, 0x4c, 0x44, 0xfe, 0xe6, 0x28, 0x80, 0xd6, 0x7a,
     0xb0, 0x30, 0x65, 0xb5, 0x8e, 0x5c, 0x54, 0x64, 0x27, 0x68, 0x4a, 0x32,
     0xac, 0xbd, 0xc2, 0xc, 0xff, 0xfb, 0x8a, 0x17, 0x89, 0xa6, 0x59, 0x3,
     0xe3, 0xbb, 0x20, 0xc7, 0x2, 0x38, 0x9a, 0x84, 0xb, 0x14, 0xc0, 0x66,
     0xd4, 0x16, 0x4b, 0x40, 0x72, 0xc8, 0xda, 0xa8, 0x86, 0xb3, 0x1a, 0x71,
     0x25, 0xd3, 0xe5, 0xe4, 0x1e, 0x50, 0xdb, 0x8, 0x26, 0x6d, 0x98, 0x60,
     0xf, 0x5b, 0x39, 0xd7, 0xe8, 0xaf, 0x73, 0xf0, 0x8f, 0x96, 0xf6, 0x7f,
     0x7, 0xb7, 0xe0, 0xfa, 0xf5, 0x70, 0xe9, 0x87, 0xa0, 0x3b, 0x46, 0xb1,
     0xe2, 0xcf, 0xe7, 0x63, 0xd1, 0x88, 0x2c, 0x6, 0x2f, 0xf7, 0x43, 0x61,
     0xde, 0x3a, 0xd5, 0x78],
    [0xcb0a16b7, 0xea150989, 0xf71e029f, 0xe3120e87, 0x639b878e, 0xd3021ea7,
     0xdf061aaf, 0x3aacb0e0, 0x3e594511, 0x6d687473, 0xc70e12bf, 0x13425e27,
     0x77978b96, 0xcbea2c4, 0x88c2de3c, 0xf41f039d, 0x2ba3bffe, 0xf3ebf76e,
     0x2ea0bcf8, 0xe914088b, 0x7b938f9e, 0x85302cc3, 0xa72e32ff, 0x6599858a,
     0x82c4d830, 0x9bda1c2, 0x93cbd72e, 0x84c6da34, 0xd1f5e952, 0x99cdd122,
     0xf81b0795, 0x35a9b5ea, 0xacdec204, 0x72948890, 0xc0fae64c, 0x44f533d,
     0x345f431d, 0x2f564a0f, 0x6c9e8284, 0x21a5b9f2, 0x325d4119, 0x9accd020,
     0x5a8c90a0, 0x66988488, 0xfd180493, 0x1db1adda, 0x3d584413, 0x517c605b,
     0x626d7179, 0x3caeb2e4, 0xb4a5637, 0x30aab6ec, 0x46716d41, 0xcfffe346,
     0x616c707b, 0xdbf3ef5e, 0x676e727f, 0x587b6755, 0xf5e9f56a, 0x538b97ae,
     0x48829ebc, 0x74e523f, 0xa3dbc70e, 0xf11c009b, 0x75607c63, 0xf0eaf66c,
     0x1a455929, 0x40736f45, 0x43726e47, 0xdc071bad, 0x80332fc5, 0x95c9d52a,
     0x983b27d5, 0x23524e07, 0xfbfa3c6, 0xa0dac60c, 0x15405c23, 0x508a96ac,
     0x1f465a2f, 0xf9edf162, 0x9b3a26d7, 0x6b8a4c8, 0x6e697571, 0x428498b0,
     0xe495531, 0x71958992, 0xa6d8c408, 0x83322ec7, 0xd0031fa5, 0x28a2befc,
     0xb7d7cb16, 0x25504c03, 0xb0233fe5, 0xba2539e9, 0x86312dc1, 0x24a6baf4,
     0x5b9a5ca, 0x44869ab4, 0x8bc3df3e, 0x78928e9c, 0xab2a36f7, 0xb92438eb,
     0x3b5a4617, 0xfaecf060, 0xa12c30fb, 0x7e908c98, 0x686b7775, 0xef160a8f,
     0x9e3925d1, 0x2a554909, 0xd4f6ea54, 0x8dc1dd3a, 0x9d3824d3, 0x90cad62c,
     0xae2935f1, 0xe4e6fa74, 0xc3fbe74e, 0xd2f4e850, 0x26514d01, 0x6a9c8080,
     0xb1d5c912, 0xafdfc306, 0x1bb3afde, 0xd485433, 0x5e796551, 0x74968a94,
     0x609a868c, 0x3bba7ce, 0x22a4b8f0, 0x7a657969, 0x5b7a6657, 0x418599b2,
     0x8f362acf, 0xccfee244, 0xa22d31f9, 0x577e625f, 0x39adb1e2, 0x9cced224,
     0xec170b8d, 0x2954480b, 0xc20d11b9, 0x893428cb, 0x45706c43, 0xfb1a0697,
     0xce0915b1, 0xf6e8f468, 0xbf263aef, 0x11b5a9d2, 0x84b5735, 0x10435f25,
     0xc5f9e54a, 0xede1fd7a, 0xa42f33fd, 0x47879bb6, 0xbdd1cd1a, 0x527d6159,
     0x17b7abd6, 0x8c372bcd, 0x73627e67, 0x18b2aedc, 0x558995aa, 0x385b4715,
     0x20534f05, 0x70637f65, 0xb5203ce3, 0x646f737d, 0x24d5139, 0x8a3529c9,
     0x33abb7ee, 0xbaa6cc, 0x81c5d932, 0xc80b17b5, 0xc6f8e448, 0xcafce040,
     0x598d91a2, 0xe5100c83, 0x5c8e92a4, 0x2da1bdfa, 0x375e421f, 0xd90418ab,
     0xe2e4f870, 0xabca0c0, 0xbc273bed, 0x8ec0dc38, 0xda0519a9, 0x943f23dd,
     0x699d8182, 0x4b839fbe, 0xc10c10bb, 0xe0130f85, 0x87c7db36, 0x76617d61,
     0xbbd3cf1e, 0xe6110d81, 0x14c503b, 0x1c475b2d, 0x4a756949, 0x9fcfd326,
     0xa9ddc102, 0x3fafb3e6, 0x4d819dba, 0x12b4a8d0, 0xf21d0199, 0x4f766a4f,
     0xb3223ee7, 0xb2d4c810, 0xe8e2fe7c, 0xebe3ff7e, 0xfe190591, 0x2c574b0d,
     0xaadcc000, 0xc40f13bd, 0xb6213de1, 0x6b6a7677, 0x6f9f8386, 0x7c677b6d,
     0xcd0814b3, 0x315c401b, 0x973e22df, 0xbed0cc18, 0xffeff366, 0x36a8b4e8,
     0x4974684b, 0xd7f7eb56, 0x568894a8, 0x7d918d9a, 0xddf1ed5a, 0x5d786453,
     0xd5001ca3, 0x1eb0acd8, 0xe7e7fb76, 0xc9fde142, 0xd8f2ee5c, 0x4c776b4d,
     0xfceef264, 0x4e809cb8, 0x27a7bbf6, 0x913c20db, 0x16415d21, 0x14b6aad4,
     0xe1e5f972, 0x96c8d428, 0xeee0fc78, 0x7964786b, 0xb4d6ca14, 0x5f8f93a6,
     0xa82b37f5, 0xd6011da1, 0xad2834f3, 0xdef0ec58, 0x1944582b, 0x7f667a6f,
     0xa5d9c50a, 0x923d21d9, 0xb8d2ce1c, 0x547f635d],
    [0xd0ab3d4, 0x12158df5, 0x191e9be8, 0x151283fc, 0x9c9b8a7c, 0x502a3cc,
     0x106abc0, 0xabace425, 0x5e591521, 0x6f687772, 0x90ebbd8, 0x4542230c,
     0x90979268, 0xb9bec013, 0xc5c23897, 0x181f99eb, 0xa4a3fa34, 0xeceb6aec,
     0xa7a0fc31, 0x13148ff6, 0x94939a64, 0x3730c79a, 0x292efbb8, 0x9e998e7a,
     0xc3c4349d, 0xbabdc616, 0xcccb2a8c, 0xc1c6309b, 0xf2f556ce, 0xcacd2686,
     0x1c1b91e7, 0xaea9ee2a, 0xd9de00b3, 0x9394946d, 0xfdfa48df, 0x484f391b,
     0x585f192b, 0x51560b30, 0x999e8073, 0xa2a5f63e, 0x5a5d1d2d, 0xcbcc2485,
     0x8b8ca445, 0x9f988c79, 0x1f1897e2, 0xb6b1de02, 0x5f581722, 0x7b7c5f4e,
     0x6a6d7d7d, 0xa9aee023, 0x4d4a3314, 0xadaae82f, 0x76714559, 0xf8ff42d0,
     0x6b6c7f7e, 0xf4f35ac4, 0x696e7b78, 0x7c7b5147, 0xeee96eea, 0x8c8baa4c,
     0x8582b857, 0x494e3b18, 0xdcdb0abc, 0x1b1c9fee, 0x6760676a, 0xedea68ef,
     0x42452d05, 0x7473415f, 0x7572435c, 0x7a9c3, 0x3433c19f, 0xcec92e8a,
     0x3c3bd187, 0x5552033c, 0xb8bfc210, 0xddda08bf, 0x4740270a, 0x8d8aa84f,
     0x41462b00, 0xeaed66e6, 0x3d3ad384, 0xbfb8cc19, 0x6e697571, 0x8384b45d,
     0x4e493511, 0x9295966e, 0xdfd80cb9, 0x3532c39c, 0x403a1cf, 0xa5a2f837,
     0xd0d712a8, 0x5750073a, 0x2423e1af, 0x2225eda5, 0x3631c599, 0xa1a6f03b,
     0xbeb9ce1a, 0x8186b05b, 0xc4c33a94, 0x95929867, 0x2d2af3b4, 0x2324efa6,
     0x5d5a1324, 0xebec64e5, 0x2b2cffbe, 0x97909c61, 0x6c6b7177, 0x11168bf0,
     0x3e39d581, 0x52550d35, 0xf1f650cb, 0xc6c13e92, 0x3f38d782, 0xcdca288f,
     0x2e29f5b1, 0xe1e670fb, 0xfcfb4adc, 0xf3f454cd, 0x56510539, 0x9b9c8475,
     0xd2d516ae, 0xd8df02b0, 0xb4b3da04, 0x4f483712, 0x7e795541, 0x9196906b,
     0x9d9a887f, 0xbcbbca1c, 0xa3a4f43d, 0x62656d65, 0x7d7a5344, 0x8285b65e,
     0x3136cb90, 0xf9fe40d3, 0x2a2dfdbd, 0x797e5b48, 0xaaade626, 0xc9ce2083,
     0x101789f3, 0x53540f36, 0xa0dbddd, 0x3334cf96, 0x7770475a, 0x1d1a93e4,
     0xe09b5d1, 0xefe86ce9, 0x2126eba0, 0xb2b5d60e, 0x4c4b3117, 0x4443210f,
     0xfef94eda, 0xe6e17ef2, 0x282ff9bb, 0x8087b258, 0xd6d11ea2, 0x7a7d5d4d,
     0xb0b7d208, 0x3037c993, 0x6562636c, 0xb5b2d807, 0x8e89ae4a, 0x5c5b1127,
     0x5453013f, 0x6463616f, 0x2720e7aa, 0x686f797b, 0x4a4d3d1d, 0x3235cd95,
     0xacabea2c, 0xbdbac81f, 0xc2c5369e, 0xc0bb1d7, 0xfff84cd9, 0xfbfc44d5,
     0x8a8da646, 0x171087fa, 0x898ea043, 0xa6a1fe32, 0x595e1b28, 0x304afc6,
     0xe3e474fd, 0xbbbcc415, 0x2027e9a3, 0xc7c03c91, 0x205adc5, 0x383fd98b,
     0x9a9d8676, 0x8483ba54, 0xb0cbfde, 0x141381ff, 0xc0c73298, 0x66616569,
     0xd4d31aa4, 0x161185f9, 0x4b4c3f1e, 0x40472903, 0x72754d55, 0xc8cf2280,
     0xdadd06b6, 0xa8afe220, 0x8681be52, 0xb3b4d40d, 0x1a1d9ded, 0x71764b50,
     0x2522e3ac, 0xd3d414ad, 0xe5e278f7, 0xe4e37af4, 0x1e1995e1, 0x50570933,
     0xdbdc04b5, 0x80fb9db, 0x2621e5a9, 0x6d6a7374, 0x989f8270, 0x60676963,
     0xf08b7d2, 0x5b5c1f2e, 0x393edb88, 0xd7d01ca1, 0xe8ef62e0, 0xafa8ec29,
     0x73744f56, 0xf0f752c8, 0x8f88ac49, 0x96919e62, 0xf6f15ec2, 0x7f785742,
     0x700a7ca, 0xb7b0dc01, 0xe0e772f8, 0xfafd46d6, 0xf5f258c7, 0x70774953,
     0xe9ee60e3, 0x8780bc51, 0xa0a7f238, 0x3b3cdf8e, 0x46412509, 0xb1b6d00b,
     0xe2e576fe, 0xcfc82c89, 0xe7e07cf1, 0x63646f66, 0xd1d610ab, 0x888fa240,
     0x2c2bf1b7, 0x601a5c9, 0x2f28f7b2, 0xf7f05cc1, 0x43442f06, 0x61666b60,
     0xded90eba, 0x3a3ddd8d, 0xd5d218a7, 0x787f594b],
    [0xdafd012, 0x1291f10d, 0x1987ec06, 0x159ff80a, 0x9c967883, 0x5bfc81a,
     0x1b7c41e, 0xabf821b4, 0x5e092541, 0x6f6b7670, 0x9a7dc16, 0x453f085a,
     0x908e6c8f, 0xb9dc17a6, 0xc52493da, 0x1885ef07, 0xa4e630bb, 0xec76e8f3,
     0xa7e035b8, 0x1393f20c, 0x9486608b, 0x37db9e28, 0x29e7bc36, 0x9e927e81,
     0xc32899dc, 0xbada12a5, 0xcc3688d3, 0xc12c9fde, 0xf24acaed, 0xca3a82d5,
     0x1c8de303, 0xaef22eb1, 0xd91cb7c6, 0x9388698c, 0xfd54dbe2, 0x48251f57,
     0x58052f47, 0x5117344e, 0x999c7786, 0xa2ea3abd, 0x5a012945, 0xcb3881d4,
     0x8bb84194, 0x9f907d80, 0x1f8be600, 0xb6c206a9, 0x5f0b2640, 0x7b434a64,
     0x6a617975, 0xa9fc27b6, 0x4d2f1052, 0xadf42bb2, 0x76595d69, 0xf85ed4e7,
     0x6b637a74, 0xf446c0eb, 0x69677c76, 0x7c4d4363, 0xee72eef1, 0x8cb64893,
     0x85a4539a, 0x49271c56, 0xdc16b8c3, 0x1b83ea04, 0x677b6e78, 0xed74ebf2,
     0x4231015d, 0x745d5b6b, 0x755f586a, 0xb5c71f, 0x34dd9b2b, 0xce328ed1,
     0x3ccd8323, 0x551f384a, 0xb8de14a7, 0xdd14bbc2, 0x473b0e58, 0x8db44b92,
     0x4137045e, 0xea7ae2f5, 0x3dcf8022, 0xbfd01da0, 0x6e697571, 0x83a8599c,
     0x4e291551, 0x928a6a8d, 0xdf10bdc0, 0x35df982a, 0x4bdcb1b, 0xa5e433ba,
     0xd00eaccf, 0x571b3e48, 0x24fdab3b, 0x22f1a13d, 0x36d99d29, 0xa1ec3fbe,
     0xbed21ea1, 0x81ac5f9e, 0xc42690db, 0x9584638a, 0x2defb032, 0x23f3a23c,
     0x5d0f2042, 0xeb78e1f4, 0x2be3ba34, 0x97806588, 0x6c6d7373, 0x1197f40e,
     0x3ec98521, 0x5211314d, 0xf14ccfee, 0xc62296d9, 0x3fcb8620, 0xcd348bd2,
     0x2ee9b531, 0xe16cfffe, 0xfc56d8e3, 0xf348c9ec, 0x56193d49, 0x9b987184,
     0xd20aaacd, 0xd81eb4c7, 0xb4c600ab, 0x4f2b1650, 0x7e494561, 0x918c6f8e,
     0x9d947b82, 0xbcd618a3, 0xa3e839bc, 0x6271617d, 0x7d4f4062, 0x82aa5a9d,
     0x31d7942e, 0xf95cd7e6, 0x2ae1b935, 0x79474c66, 0xaafa22b5, 0xc93c87d6,
     0x1095f70f, 0x5313324c, 0xaa1d915, 0x33d3922c, 0x775b5e68, 0x1d8fe002,
     0xea9d511, 0xef70edf0, 0x21f7a43e, 0xb2ca0aad, 0x4c2d1353, 0x443d0b5b,
     0xfe52dee1, 0xe662f6f9, 0x28e5bf37, 0x80ae5c9f, 0xd602a6c9, 0x7a414965,
     0xb0ce0caf, 0x30d5972f, 0x657f687a, 0xb5c403aa, 0x8eb24e91, 0x5c0d2343,
     0x541d3b4b, 0x647d6b7b, 0x27fbae38, 0x68657f77, 0x4a211955, 0x32d1912d,
     0xacf628b3, 0xbdd41ba2, 0xc22a9add, 0xcadd313, 0xff50dde0, 0xfb58d1e4,
     0x8aba4295, 0x179bfe08, 0x89bc4796, 0xa6e236b9, 0x59072c46, 0x3b3c21c,
     0xe368f9fc, 0xbbd811a4, 0x20f5a73f, 0xc72095d8, 0x2b1c11d, 0x38c58f27,
     0x9a9a7285, 0x84a6509b, 0xba3da14, 0x149dfb0b, 0xc02e9cdf, 0x66796d79,
     0xd406a0cb, 0x1699fd09, 0x4b231a54, 0x4035075f, 0x7251516d, 0xc83e84d7,
     0xda1ab2c5, 0xa8fe24b7, 0x86a25699, 0xb3c809ac, 0x1a81e905, 0x7157546e,
     0x25ffa83a, 0xd308a9cc, 0xe564f3fa, 0xe466f0fb, 0x1e89e501, 0x5015374f,
     0xdb18b1c4, 0x8a5df17, 0x26f9ad39, 0x6d6f7072, 0x989e7487, 0x6075677f,
     0xfabd610, 0x5b032a44, 0x39c78c26, 0xd700a5c8, 0xe87ee4f7, 0xaff02db0,
     0x7353526c, 0xf04eccef, 0x8fb04d90, 0x96826689, 0xf642c6e9, 0x7f4b4660,
     0x7bbce18, 0xb7c005a8, 0xe06efcff, 0xfa5ad2e5, 0xf544c3ea, 0x7055576f,
     0xe97ce7f6, 0x87a05598, 0xa0ee3cbf, 0x3bc38a24, 0x46390d59, 0xb1cc0fae,
     0xe26afafd, 0xcf308dd0, 0xe760f5f8, 0x6373627c, 0xd10cafce, 0x88be4497,
     0x2cedb333, 0x6b9cd19, 0x2febb630, 0xf740c5e8, 0x4333025c, 0x6177647e,
     0xde12bec1, 0x3ac18925, 0xd504a3ca, 0x78454f67],
    [0x346e754c, 0x77334e72, 0x72343359, 0x38316f32, 0x1769b2e5, 0x605afc97,
     0x126ecfce, 0x2a5fa0fc, 0xa78c7d07, 0xc7d68190, 0xd5b84e5e, 0xffe7eea2,
     0x9d9ae92b, 0x5a4c68bb, 0x8ff426e5, 0x7013c847, 0x3dcb94cb, 0x6787fc70,
     0xe873da95, 0x986012d2, 0x888d4412, 0xef0ab862, 0x77962f7, 0x9f197025,
     0xb7569063, 0x585c2801, 0x5f254af6, 0xc03c3ad3, 0xd1ec7ba3, 0x89b053a2,
     0xd6951954, 0x16a92387, 0xc6aba805, 0x4f1bfba7, 0x998ee2f3, 0x8f27c174,
     0x54d86466, 0x1bc39fc1, 0x824d7d32, 0xd6abc46, 0x6061085b, 0x7ba2979a,
     0xf9efeaa8, 0xf48556ee],
    [0xa8cc1612, 0x96ed090d, 0x80f00206, 0x98e40e0a, 0x91648783, 0xb8d41e1a,
     0xb0d81a1e, 0xff3db0b4, 0xe394541, 0x6c6a7470, 0xa0c01216, 0x38145e5a,
     0x89708b8f, 0xdb0ba2a6, 0x238fdeda, 0x82f30307, 0xe12cbfbb, 0x71f4f7f3,
     0xe729bcb8, 0x94ee080c, 0x817c8f8b, 0xdc822c28, 0xe0a03236, 0x95628581,
     0x2f85d8dc, 0xdd0ea1a5, 0x3194d7d3, 0x2b83dade, 0x4dd6e9ed, 0x3d9ed1d5,
     0x8aff0703, 0xf532b5b1, 0x1babc2c6, 0x8f75888c, 0x53c7e6e2, 0x22035357,
     0x2334347, 0x10284a4e, 0x9b6b8286, 0xed26b9bd, 0x6354145, 0x3f9dd0d4,
     0xbf5d9094, 0x97618480, 0x8cfa0400, 0xc51aada9, 0xc3a4440, 0x44566064,
     0x66657175, 0xfb3bb2b6, 0x280c5652, 0xf337b6b2, 0x5e416d69, 0x59c8e3e7,
     0x64667074, 0x41dcefeb, 0x60607276, 0x4a5f6763, 0x75f2f5f1, 0xb1549793,
     0xa34f9e9a, 0x20005256, 0x11a4c7c3, 0x84f60004, 0x7c727c78, 0x73f7f6f2,
     0x361d595d, 0x5a476f6b, 0x58446e6a, 0xb2db1b1f, 0xda872f2b, 0x3592d5d1,
     0xca9f2723, 0x18244e4a, 0xd908a3a7, 0x13a7c6c2, 0x3c125c58, 0xb3579692,
     0x30185a5e, 0x7dfef1f5, 0xc89c2622, 0xd701a4a0, 0x6e697571, 0xaf45989c,
     0x2e095551, 0x8d76898d, 0x17a1c4c0, 0xd8842e2a, 0xbad71f1b, 0xe32fbeba,
     0x9b0cbcf, 0x1c224c48, 0xfab73f3b, 0xf6bd393d, 0xde812d29, 0xeb23babe,
     0xd502a5a1, 0xab439a9e, 0x218cdfdb, 0x837f8e8a, 0xe8ac3632, 0xf4be383c,
     0x83c4642, 0x7ffdf0f4, 0xe4a63034, 0x87798c88, 0x6a6f7773, 0x90e80a0e,
     0xce992521, 0x162d494d, 0x4bd3eaee, 0x258addd9, 0xcc9a2420, 0x3397d6d2,
     0xeea93531, 0x6be3fafe, 0x51c4e7e3, 0x4fd5e8ec, 0x1e214d49, 0x9f6d8084,
     0xdb6c9cd, 0x19a8c3c7, 0xc11cafab, 0x2c0a5450, 0x4e596561, 0x8b738a8e,
     0x93678682, 0xd104a7a3, 0xef25b8bc, 0x767d797d, 0x485c6662, 0xad46999d,
     0xd0882a2e, 0x5bcbe2e6, 0xe6a53135, 0x40506266, 0xfd3eb1b5, 0x3b9bd2d6,
     0x92eb0b0f, 0x142e484c, 0xa6c51115, 0xd48e282c, 0x5c426c68, 0x88fc0602,
     0xaec91511, 0x77f1f4f0, 0xf0b83a3e, 0xcd16a9ad, 0x2a0f5753, 0x3a175f5b,
     0x55c2e5e1, 0x65eafdf9, 0xe2a33337, 0xa9409b9f, 0x5bacdc9, 0x46556165,
     0xc910abaf, 0xd28b2b2f, 0x78747e7a, 0xc31faeaa, 0xb5529591, 0xa3f4743,
     0x1a274f4b, 0x7a777f7b, 0xfcb23c38, 0x62637377, 0x26055155, 0xd68d292d,
     0xf134b7b3, 0xd307a6a2, 0x2d86d9dd, 0xaacf1713, 0x57c1e4e0, 0x5fcde0e4,
     0xbd5e9195, 0x9ce20c08, 0xbb5b9296, 0xe52abdb9, 0x304246, 0xb4de181c,
     0x6fe5f8fc, 0xdf0da0a4, 0xf2bb3b3f, 0x2789dcd8, 0xb6dd191d, 0xc2932327,
     0x9d6e8185, 0xa14c9f9b, 0xa4c61014, 0x9ae70f0b, 0x2980dbdf, 0x7e717d79,
     0x1bccfcb, 0x9ee10d09, 0x24065054, 0x321b5b5f, 0x564d696d, 0x3998d3d7,
     0x1daec1c5, 0xf938b3b7, 0xa54a9d99, 0xcf15a8ac, 0x86f50105, 0x50486a6e,
     0xf8b43e3a, 0xfb5c8cc, 0x63effefa, 0x61ecfffb, 0x8ef90501, 0x122b4b4f,
     0x1fadc0c4, 0xa2c31317, 0xfeb13d39, 0x686c7672, 0x99688387, 0x727b7b7f,
     0xacca1410, 0x4364044, 0xc0902226, 0x7b9ccc8, 0x79f8f3f7, 0xf731b4b0,
     0x544e686c, 0x49d0ebef, 0xb7519490, 0x857a8d89, 0x45daede9, 0x4c5a6460,
     0xbcd21c18, 0xc719aca8, 0x69e0fbff, 0x5dcee1e5, 0x43dfeeea, 0x524b6b6f,
     0x7bfbf2f6, 0xa7499c98, 0xe920bbbf, 0xc4962024, 0x3e115d59, 0xcb13aaae,
     0x6de6f9fd, 0x3791d4d0, 0x67e9fcf8, 0x747e787c, 0xbb3cace, 0xb9589397,
     0xeaaf3733, 0xbed11d19, 0xecaa3430, 0x47d9ece8, 0x341e585c, 0x70787a7e,
     0x15a2c5c1, 0xc6952125, 0x3bfceca, 0x42536367]]


def permute(src):
    w0 = struct.unpack("I", bytearray(src[0:4]))[0]
    w1 = struct.unpack("I", bytearray(src[4:8]))[0]
    w2 = struct.unpack("I", bytearray(src[8:12]))[0]
    w3 = struct.unpack("I", bytearray(src[12:16]))[0]
    t0 = ((tbl[1][((w0) & 0xff)] ^ tbl[2][(((w1) >> 8) & 0xff)] ^ tbl[3][(
        ((w2) >> 16) & 0xff)] ^ tbl[5][(((w3) >> 24) & 0xff)]) ^ (tbl[4][4]))
    t1 = ((tbl[1][((w1) & 0xff)] ^ tbl[2][(((w2) >> 8) & 0xff)] ^ tbl[3][(
        ((w3) >> 16) & 0xff)] ^ tbl[5][(((w0) >> 24) & 0xff)]) ^ (tbl[4][5]))
    t2 = ((tbl[1][((w2) & 0xff)] ^ tbl[2][(((w3) >> 8) & 0xff)] ^ tbl[3][(
        ((w0) >> 16) & 0xff)] ^ tbl[5][(((w1) >> 24) & 0xff)]) ^ (tbl[4][6]))
    t3 = ((tbl[1][((w3) & 0xff)] ^ tbl[2][(((w0) >> 8) & 0xff)] ^ tbl[3][(
        ((w1) >> 16) & 0xff)] ^ tbl[5][(((w2) >> 24) & 0xff)]) ^ (tbl[4][7]))
    w0 = t0
    w1 = t1
    w2 = t2
    w3 = t3
    t0 = ((tbl[1][((w0) & 0xff)] ^ tbl[2][(((w1) >> 8) & 0xff)] ^ tbl[3][(
        ((w2) >> 16) & 0xff)] ^ tbl[5][(((w3) >> 24) & 0xff)]) ^ (tbl[4][8]))
    t1 = ((tbl[1][((w1) & 0xff)] ^ tbl[2][(((w2) >> 8) & 0xff)] ^ tbl[3][(
        ((w3) >> 16) & 0xff)] ^ tbl[5][(((w0) >> 24) & 0xff)]) ^ (tbl[4][9]))
    t2 = ((tbl[1][((w2) & 0xff)] ^ tbl[2][(((w3) >> 8) & 0xff)] ^ tbl[3][(
        ((w0) >> 16) & 0xff)] ^ tbl[5][(((w1) >> 24) & 0xff)]) ^ (tbl[4][10]))
    t3 = ((tbl[1][((w3) & 0xff)] ^ tbl[2][(((w0) >> 8) & 0xff)] ^ tbl[3][(
        ((w1) >> 16) & 0xff)] ^ tbl[5][(((w2) >> 24) & 0xff)]) ^ (tbl[4][11]))
    w0 = t0
    w1 = t1
    w2 = t2
    w3 = t3
    t0 = ((tbl[1][((w0) & 0xff)] ^ tbl[2][(((w1) >> 8) & 0xff)] ^ tbl[3][(
        ((w2) >> 16) & 0xff)] ^ tbl[5][(((w3) >> 24) & 0xff)]) ^ (tbl[4][12]))
    t1 = ((tbl[1][((w1) & 0xff)] ^ tbl[2][(((w2) >> 8) & 0xff)] ^ tbl[3][(
        ((w3) >> 16) & 0xff)] ^ tbl[5][(((w0) >> 24) & 0xff)]) ^ (tbl[4][13]))
    t2 = ((tbl[1][((w2) & 0xff)] ^ tbl[2][(((w3) >> 8) & 0xff)] ^ tbl[3][(
        ((w0) >> 16) & 0xff)] ^ tbl[5][(((w1) >> 24) & 0xff)]) ^ (tbl[4][14]))
    t3 = ((tbl[1][((w3) & 0xff)] ^ tbl[2][(((w0) >> 8) & 0xff)] ^ tbl[3][(
        ((w1) >> 16) & 0xff)] ^ tbl[5][(((w2) >> 24) & 0xff)]) ^ (tbl[4][15]))
    w0 = t0
    w1 = t1
    w2 = t2
    w3 = t3
    t0 = ((tbl[1][((w0) & 0xff)] ^ tbl[2][(((w1) >> 8) & 0xff)] ^ tbl[3][(
        ((w2) >> 16) & 0xff)] ^ tbl[5][(((w3) >> 24) & 0xff)]) ^ (tbl[4][16]))
    t1 = ((tbl[1][((w1) & 0xff)] ^ tbl[2][(((w2) >> 8) & 0xff)] ^ tbl[3][(
        ((w3) >> 16) & 0xff)] ^ tbl[5][(((w0) >> 24) & 0xff)]) ^ (tbl[4][17]))
    t2 = ((tbl[1][((w2) & 0xff)] ^ tbl[2][(((w3) >> 8) & 0xff)] ^ tbl[3][(
        ((w0) >> 16) & 0xff)] ^ tbl[5][(((w1) >> 24) & 0xff)]) ^ (tbl[4][18]))
    t3 = ((tbl[1][((w3) & 0xff)] ^ tbl[2][(((w0) >> 8) & 0xff)] ^ tbl[3][(
        ((w1) >> 16) & 0xff)] ^ tbl[5][(((w2) >> 24) & 0xff)]) ^ (tbl[4][19]))
    w0 = t0
    w1 = t1
    w2 = t2
    w3 = t3
    t0 = ((tbl[1][((w0) & 0xff)] ^ tbl[2][(((w1) >> 8) & 0xff)] ^ tbl[3][(
        ((w2) >> 16) & 0xff)] ^ tbl[5][(((w3) >> 24) & 0xff)]) ^ (tbl[4][20]))
    t1 = ((tbl[1][((w1) & 0xff)] ^ tbl[2][(((w2) >> 8) & 0xff)] ^ tbl[3][(
        ((w3) >> 16) & 0xff)] ^ tbl[5][(((w0) >> 24) & 0xff)]) ^ (tbl[4][21]))
    t2 = ((tbl[1][((w2) & 0xff)] ^ tbl[2][(((w3) >> 8) & 0xff)] ^ tbl[3][(
        ((w0) >> 16) & 0xff)] ^ tbl[5][(((w1) >> 24) & 0xff)]) ^ (tbl[4][22]))
    t3 = ((tbl[1][((w3) & 0xff)] ^ tbl[2][(((w0) >> 8) & 0xff)] ^ tbl[3][(
        ((w1) >> 16) & 0xff)] ^ tbl[5][(((w2) >> 24) & 0xff)]) ^ (tbl[4][23]))
    w0 = t0
    w1 = t1
    w2 = t2
    w3 = t3
    t0 = ((tbl[1][((w0) & 0xff)] ^ tbl[2][(((w1) >> 8) & 0xff)] ^ tbl[3][(
        ((w2) >> 16) & 0xff)] ^ tbl[5][(((w3) >> 24) & 0xff)]) ^ (tbl[4][24]))
    t1 = ((tbl[1][((w1) & 0xff)] ^ tbl[2][(((w2) >> 8) & 0xff)] ^ tbl[3][(
        ((w3) >> 16) & 0xff)] ^ tbl[5][(((w0) >> 24) & 0xff)]) ^ (tbl[4][25]))
    t2 = ((tbl[1][((w2) & 0xff)] ^ tbl[2][(((w3) >> 8) & 0xff)] ^ tbl[3][(
        ((w0) >> 16) & 0xff)] ^ tbl[5][(((w1) >> 24) & 0xff)]) ^ (tbl[4][26]))
    t3 = ((tbl[1][((w3) & 0xff)] ^ tbl[2][(((w0) >> 8) & 0xff)] ^ tbl[3][(
        ((w1) >> 16) & 0xff)] ^ tbl[5][(((w2) >> 24) & 0xff)]) ^ (tbl[4][27]))
    w0 = t0
    w1 = t1
    w2 = t2
    w3 = t3
    t0 = ((tbl[1][((w0) & 0xff)] ^ tbl[2][(((w1) >> 8) & 0xff)] ^ tbl[3][(
        ((w2) >> 16) & 0xff)] ^ tbl[5][(((w3) >> 24) & 0xff)]) ^ (tbl[4][28]))
    t1 = ((tbl[1][((w1) & 0xff)] ^ tbl[2][(((w2) >> 8) & 0xff)] ^ tbl[3][(
        ((w3) >> 16) & 0xff)] ^ tbl[5][(((w0) >> 24) & 0xff)]) ^ (tbl[4][29]))
    t2 = ((tbl[1][((w2) & 0xff)] ^ tbl[2][(((w3) >> 8) & 0xff)] ^ tbl[3][(
        ((w0) >> 16) & 0xff)] ^ tbl[5][(((w1) >> 24) & 0xff)]) ^ (tbl[4][30]))
    t3 = ((tbl[1][((w3) & 0xff)] ^ tbl[2][(((w0) >> 8) & 0xff)] ^ tbl[3][(
        ((w1) >> 16) & 0xff)] ^ tbl[5][(((w2) >> 24) & 0xff)]) ^ (tbl[4][31]))
    w0 = t0
    w1 = t1
    w2 = t2
    w3 = t3
    t0 = ((tbl[1][((w0) & 0xff)] ^ tbl[2][(((w1) >> 8) & 0xff)] ^ tbl[3][(
        ((w2) >> 16) & 0xff)] ^ tbl[5][(((w3) >> 24) & 0xff)]) ^ (tbl[4][32]))
    t1 = ((tbl[1][((w1) & 0xff)] ^ tbl[2][(((w2) >> 8) & 0xff)] ^ tbl[3][(
        ((w3) >> 16) & 0xff)] ^ tbl[5][(((w0) >> 24) & 0xff)]) ^ (tbl[4][33]))
    t2 = ((tbl[1][((w2) & 0xff)] ^ tbl[2][(((w3) >> 8) & 0xff)] ^ tbl[3][(
        ((w0) >> 16) & 0xff)] ^ tbl[5][(((w1) >> 24) & 0xff)]) ^ (tbl[4][34]))
    t3 = ((tbl[1][((w3) & 0xff)] ^ tbl[2][(((w0) >> 8) & 0xff)] ^ tbl[3][(
        ((w1) >> 16) & 0xff)] ^ tbl[5][(((w2) >> 24) & 0xff)]) ^ (tbl[4][35]))
    w0 = t0
    w1 = t1
    w2 = t2
    w3 = t3
    t0 = ((tbl[1][((w0) & 0xff)] ^ tbl[2][(((w1) >> 8) & 0xff)] ^ tbl[3][(
        ((w2) >> 16) & 0xff)] ^ tbl[5][(((w3) >> 24) & 0xff)]) ^ (tbl[4][36]))
    t1 = ((tbl[1][((w1) & 0xff)] ^ tbl[2][(((w2) >> 8) & 0xff)] ^ tbl[3][(
        ((w3) >> 16) & 0xff)] ^ tbl[5][(((w0) >> 24) & 0xff)]) ^ (tbl[4][37]))
    t2 = ((tbl[1][((w2) & 0xff)] ^ tbl[2][(((w3) >> 8) & 0xff)] ^ tbl[3][(
        ((w0) >> 16) & 0xff)] ^ tbl[5][(((w1) >> 24) & 0xff)]) ^ (tbl[4][38]))
    t3 = ((tbl[1][((w3) & 0xff)] ^ tbl[2][(((w0) >> 8) & 0xff)] ^ tbl[3][(
        ((w1) >> 16) & 0xff)] ^ tbl[5][(((w2) >> 24) & 0xff)]) ^ (tbl[4][39]))
    w0 = t0
    w1 = t1
    w2 = t2
    w3 = t3
    t0 = (((tbl[0][((w0) & 0xff)]) | ((tbl[0][(((w1) >> 8) & 0xff)]) << 8) | ((
        tbl[0][(((w2) >> 16) & 0xff)]) << 16) | ((tbl[0][(((w3) >> 24) & 0xff)]) << 24)) ^ (tbl[4][40]))
    t1 = (((tbl[0][((w1) & 0xff)]) | ((tbl[0][(((w2) >> 8) & 0xff)]) << 8) | ((
        tbl[0][(((w3) >> 16) & 0xff)]) << 16) | ((tbl[0][(((w0) >> 24) & 0xff)]) << 24)) ^ (tbl[4][41]))
    t2 = (((tbl[0][((w2) & 0xff)]) | ((tbl[0][(((w3) >> 8) & 0xff)]) << 8) | ((
        tbl[0][(((w0) >> 16) & 0xff)]) << 16) | ((tbl[0][(((w1) >> 24) & 0xff)]) << 24)) ^ (tbl[4][42]))
    t3 = (((tbl[0][((w3) & 0xff)]) | ((tbl[0][(((w0) >> 8) & 0xff)]) << 8) | ((
        tbl[0][(((w1) >> 16) & 0xff)]) << 16) | ((tbl[0][(((w2) >> 24) & 0xff)]) << 24)) ^ (tbl[4][43]))
    cipher = ([(t0 >> i & 0xff) for i in (0, 8, 16, 24)] +
              [(t1 >> i & 0xff) for i in (0, 8, 16, 24)] +
              [(t2 >> i & 0xff) for i in (0, 8, 16, 24)] +
              [(t3 >> i & 0xff) for i in (0, 8, 16, 24)])

    return cipher


def xor(a, b):
    assert len(a) == len(b)
    return [x[0] ^ x[1] for x in zip(a, b)]


names = [
    "Việt Nam",
    "Đại Nam",
    "Đại Việt",
    "Đại Cồ Việt",
    "Vạn Xuân",
    "Lĩnh Nam",
    "Âu Lạc",
    "Văn Lang",
]


def vn_x931():
    seed = struct.unpack("<16B", bytearray(os.urandom(16)))
    # print seed
    v = seed
    s = []
    for name in reversed(names):
        trucated = hashlib.sha256(name).hexdigest()[0:32]
        t = permute(map(ord, trucated.decode('hex')))
        r = permute(xor(t, v))
        v = permute(xor(t, r))
        s.append(binascii.hexlify(bytearray(r)))
    return s[0:-1], s[-1]

# I add this for debug purpose
if __name__ == '__main__':
    cs, s = vn_x931()
    print s
    for i in reversed(cs):
        print i
