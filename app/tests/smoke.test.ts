import {describe,it,expect} from 'vitest';
import rooms from '../src/rooms.json';
describe('fixture phòng',()=>{it('khớp trạng thái sảnh mặc định',()=>{expect(rooms).toHaveLength(4);expect(rooms.filter(r=>r.status==='waiting'&&r.playerIds.length<r.maxPlayers)).toHaveLength(2);expect(rooms.filter(r=>r.status==='playing')).toHaveLength(1);expect(rooms.filter(r=>r.status==='waiting'&&r.playerIds.length>=r.maxPlayers)).toHaveLength(1)})});
