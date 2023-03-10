import {
Box,
Flex,
Link,
Button,
Stack,
useColorModeValue,
useDisclosure,
Icon,
IconButton,
Menu,
MenuButton,
MenuList,
MenuItem,
MenuDivider,
Avatar,
} from '@chakra-ui/react';
import { HamburgerIcon, CloseIcon } from '@chakra-ui/icons';
import { FiLogIn, FiShoppingCart } from 'react-icons/fi';

export default function Navbar() {
const sections = [
{
name: 'Product',
href: '/product',
},
{
name: 'Pricing',
href: '/pricing',
},
];
const { isOpen, onToggle } = useDisclosure();

return (
<>
<Box
bg={useColorModeValue('gray.100', 'gray.900')}
px={4}
py={3}
borderBottom={'1px'}
borderBottomColor={useColorModeValue('gray.200', 'gray.700')}>
<Flex
h={16}
alignItems={'center'}
justifyContent={'space-between'}>
<Flex alignItems={'center'}>
<Link
mr={8}
fontWeight="bold"
name="Product"
href="/product"
fontSize="2xl"
color={useColorModeValue('gray.700', 'white')}>
Vercel
</Link>
<Stack as={'nav'} direction={'row'} spacing={4}>
{sections.map((section) => (
<Link
key={section.name}
href={section.href}
fontSize={'xl'}
fontWeight={600}
color={useColorModeValue('gray.600', 'gray.200')}
_hover={{
textDecoration: 'none',
color: useColorModeValue('gray.800', 'white'),
}}>
{section.name}
</Link>
))}
</Stack>
</Flex>

<Box>
<Menu>
<MenuButton
as={Button}
rounded={'full'}
variant={'link'}
cursor={'pointer'}
minW={0}>
<Avatar
size={'sm'}
src={
'https://images.unsplash.com/photo-1493666438817-866a91353ca9?ixlib=rb-0.3.5&q=80&fm=jpg&crop=faces&fit=crop&h=200&w=200&s=b616b2c5b373a80ffc9636ba24f7a4a9'
}
/>
</MenuButton>
<MenuList>
<MenuItem>Profile</MenuItem>
<MenuItem>Settings</MenuItem>
<MenuDivider />
<MenuItem>Sign Out</MenuItem>
</MenuList>
</Menu>
</Box>

<Flex
display={{ base: 'none', md: 'flex' }}
ml={10}
alignItems={'center'}>
<Link
fontSize={'xl'}
fontWeight={600}
color={'green.500'}
href={'/'}>
Subscribe
<Icon
as={FiShoppingCart}
color={useColorModeValue('gray.600', 'gray.200')}
ml={3}
/>
</Link>
<Button
leftIcon={<FiLogIn />}
bg={'green.500'}
color={'white'}
px={5}
_hover={{
bg: 'green.600',
}}>
Sign in
</Button>
</Flex>

<IconButton
size={'md'}
icon={isOpen ? <CloseIcon /> : <HamburgerIcon />}
aria-label={'Open Menu'}
display={{ md: 'none' }}
onClick={onToggle}
/>
</Flex>

{isOpen ? (
<Box pb={4} display={{ md: 'none' }}>
<Stack as={'nav'} spacing={4}>
{sections.map((section) => (
<Link
key={section.name}
href={section.href}
fontSize={'xl'}
fontWeight={600}
color={useColorModeValue('gray.600', 'gray.200')}
_hover={{
textDecoration: 'none',
color: useColorModeValue('gray.800', 'white'),
}}>
{section.name}
</Link>
))}
<Button
leftIcon={<FiLogIn />}
bg={'green.500'}
color={'white'}
mt={4}
px={5}
_hover={{
bg: 'green.600',
}}>
Sign in
</Button>
<Link
mt={4}
fontSize={'xl'}
fontWeight={600}
color={'green.500'}
href={'/'}>
Subscribe
<Icon
as={FiShoppingCart}
color={useColorModeValue('gray.600', 'gray.200')}
ml={3}
/>
</Link>
</Stack>
</Box>
) : null}
</Box>
</>
);
}