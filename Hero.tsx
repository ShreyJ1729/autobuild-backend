import {
  Flex,
  Button,
  Text,
  VStack,
  useBreakpointValue,
} from '@chakra-ui/react';

export default function Hero() {
  return (
<Flex
  w={'full'}
  h={'100vh'}
  backgroundImage={
'url(https://images.unsplash.com/photo-1525051155559-ae8d2853b2e1?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTZ8fGJsb29kJTIwYW5kJTIwd2hpdGUlMjBzdG9yeXxlbnwwfHw&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80)'
  }
  backgroundSize={'cover'}
  backgroundPosition={'center center'}>
  <VStack
w={'full'}
justify={'center'}
px={useBreakpointValue({ base: 4, md: 8 })}
bgGradient={'linear(to-r, teal.300, teal.900)'}>
<Text
  fontWeight={700}
  fontSize={useBreakpointValue({ base: '3xl', md: '4xl', lg: '6xl' })}
  lineHeight={1.2}
  color={'white'}>
  Vercel{' '}
<Text as={'span'} color={'teal.500'}>
  - The Platform for Frontend Developers
</Text>
</Text>
<Text
  fontSize={useBreakpointValue({ base: 'md', md: 'lg' })}
  color={'white'}>
  Providing speed and reliability to shipping products through instant
  deployment and automatic scaling.
</Text>
<Button
  bg={'teal.400'}
  rounded={'full'}
  color={'white'}
  _hover={{ bg: 'teal.500' }}>
  Get started
</Button>
  </VStack>
</Flex>
  );
}