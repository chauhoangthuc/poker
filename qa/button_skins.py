from pathlib import Path
from shutil import copyfile
root=Path('app/public/assets/buttons');root.mkdir(parents=True,exist_ok=True)
source=Path(r'C:\Users\BDPC\.codex\generated_images\01a1882f-5513-7d70-9166-b9fb73f71584')
for name,file in [('play','exec-721ecbe0-a950-4e6d-89b3-80287d125d1e.png'),('violet','exec-a0eeb99a-881e-4ea6-891c-147dfc238ec5.png'),('navy','exec-9f3a5115-28f4-42b2-9aab-1b19b79347ce.png')]:copyfile(source/file,root/(name+'.png'))
p=Path('app/src/Button.tsx');s=p.read_text(encoding='utf-8-sig');s=s.replace('variant?:Variant;','skin?:"play"|"violet"|"navy";variant?:Variant;').replace("Button({variant='tertiary'","Button({skin,variant='tertiary'");s=s.replace('className={`${buttonVariants(variant,size)}','className={`${skin ? `png-skin skin-${skin}` : ""} ${buttonVariants(variant,size)}');p.write_text(s,encoding='utf-8')
p=Path('app/src/RoomArena.tsx');s=p.read_text(encoding='utf-8-sig');s=s.replace('<Button size="lg" leadingIcon={<Layers/>}', '<Button skin="navy" size="lg" leadingIcon={<Layers/>}').replace('<Button variant="secondary" size="lg" leadingIcon={<Ban/>}', '<Button skin="violet" variant="secondary" size="lg" leadingIcon={<Ban/>}').replace('<Button variant="primary" size="lg" leadingIcon={<span className="play-spade">♠</span>}', '<Button skin="play" variant="primary" size="lg"');p.write_text(s,encoding='utf-8')
